# Selenium에서 필요한 모듈
from selenium import webdriver  # 웹 드라이버 관련 모듈
from selenium.webdriver.chrome.service import Service  # Chrome 서비스 관련 모듈
from selenium.webdriver.chrome.options import Options  # Chrome 옵션 관련 모듈
from selenium.webdriver.common.by import By  # 웹 요소를 검색하기 위한 방법(By) 관련 모듈
from selenium.webdriver.support.ui import WebDriverWait  # 웹 페이지가 로드될 때까지 대기하기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC  # 조건을 기다리기 위한 모듈
from selenium.webdriver.common.action_chains import ActionChains  # 마우스 액션을 수행하기 위한 모듈

# BeautifulSoup를 사용하여 HTML 파싱을 위한 모듈
from bs4 import BeautifulSoup

# 정규 표현식 및 시간 관련 모듈
import re
import time

# GUI 요소를 생성하기 위한 모듈
import tkinter as tk
from tkinter import Menu, Button, Text, Scrollbar, BooleanVar, messagebox, filedialog

# 다중 스레드를 위한 threading 모듈
import threading



def split_desc(desc):
    parts = desc.split('|')
    release_date = parts[0].strip() if len(parts) > 0 else 'N/A'
    track_count = parts[2].strip() if len(parts) > 2 else 'N/A'
    return release_date, track_count



def fetch_album_info(url, text_area, delete_url_after_download, url_entry, delay):
    chrome_driver_path = r'./ChromeDriver/chromedriver.exe'  # ChromeDriver 상대 경로

    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    try:
        time.sleep(delay)  # delay 초 동안 대기
        
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        
        driver.get(url)

        # 가수 이름 가져오기
        try:
            artist_element = driver.find_element(By.CSS_SELECTOR, 'h2.page-top-this a')
            artist_name = artist_element.text.strip() if artist_element else 'Unknown Artist'
        except Exception as e:
            artist_name = 'Unknown Artist'
        
        album_info_list = []
        
        while True:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.list-album')))
                
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                
                albums = soup.select('li.list-album')
                
                if not albums:
                    text_area.insert(tk.END, "[안내] 페이지에서 앨범을 찾을 수 없습니다.\n")
                    text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                    break

                for album in albums:
                    title = album.select_one('dt.ellipsis a').get_text(strip=True)
                    desc = album.select_one('dd.desc').get_text(strip=True)
                    release_date, track_count = split_desc(desc)
                    
                    album_link = album.select_one('a[onclick]')
                    fn_view_album_layer = 'N/A'
                    if album_link and 'onclick' in album_link.attrs:
                        onclick_text = album_link['onclick']
                        match = re.search(r"fnViewAlbumLayer\('(\d+)'\)", onclick_text)
                        if match:
                            fn_view_album_layer = match.group(1)
                    
                    album_info_list.append({
                        'Title': title,
                        'Release Date': release_date,
                        'Track Count': track_count,
                        'fnViewAlbumLayer': fn_view_album_layer
                    })

                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, 'a.next')
                    if next_button:
                        ActionChains(driver).move_to_element(next_button).click().perform()
                        time.sleep(2)
                    else:
                        break
                except Exception as e:
                    text_area.insert(tk.END, f"[경고] 다음 페이지로 이동하는 버튼을 찾을 수 없거나 다른 문제가 발생하였습니다.: {e}\n")
                    text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                    break

            except Exception as e:
                text_area.insert(tk.END, f"[알림] 예외 발생: {e}\n\n\n")
                try:
                    alert = driver.switch_to.alert
                    alert_text = alert.text
                    alert.accept()
                    text_area.insert(tk.END, f"[안내] 알림이 수락되었습니다: {alert_text}\n\n")
                    if "마지막 페이지입니다" in alert_text:
                        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                        break
                except Exception as alert_exception:
                    text_area.insert(tk.END, f"[안내] Failed to handle alert: {alert_exception}\n\n\n")
                    text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                break

        if album_info_list:
            # text_area 초기화
            text_area.delete(1.0, tk.END)
            
            text_area.insert(tk.END, f"\n[알림] 모든 작업이 정상적으로 처리되었습니다.\n\n\n\n")

            text_area.insert(tk.END, f"===== {artist_name} Album Information =====\n\n")
            
            for album_info in album_info_list:
                text_area.insert(tk.END, '-' * 40 + '\n')
                text_area.insert(tk.END, f"Title: {album_info['Title']}\n")
                text_area.insert(tk.END, f"Release Date: {album_info['Release Date']}\n")
                text_area.insert(tk.END, f"Track Count: {album_info['Track Count']}\n")
                text_area.insert(tk.END, f"Album Info: {album_info['fnViewAlbumLayer']}\n")
                text_area.insert(tk.END, f"\n[Album URL]\nhttps://www.genie.co.kr/detail/albumInfo?axnm={album_info['fnViewAlbumLayer']}\n")
                text_area.insert(tk.END, '-' * 40 + '\n\n')

        else:
            text_area.insert(tk.END, "[안내] 앨범 정보를 찾을 수 없습니다.\n\n")
            text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
    
    finally:
        # 작업이 끝난 후에 버튼 다시 활성화
        url_entry.config(state=tk.NORMAL)
        fetch_button.config(state=tk.NORMAL)
        button_clear.config(state=tk.NORMAL)
        
        if delete_url_after_download.get():
            url_entry.delete(0, tk.END)
            
        driver.quit()



def start_fetching(url_entry, text_area, delete_url_after_download):
    url = url_entry.get()
    if url.startswith('https://www.genie.co.kr/detail/artistAlbum?xxnm='):
        
        # 앨범 정보 가져오기 버튼 비활성화
        url_entry.config(state=tk.DISABLED)
        fetch_button.config(state=tk.DISABLED)
        button_clear.config(state=tk.DISABLED)

        # 지연 시간 설정 (초 단위)
        delay = 5
        
        text_area.insert(tk.END, f"\n[알림] {delay}초 후 작업이 진행 됩니다.\n\n")
        text_area.insert(tk.END, f"[경고] 작업이 진행되는 웹 브라우저를 임의로 작업하지 마십시오.\n\n")
        # text_area.insert(tk.END, "[알림] 아래에 표기 된 내용은 오류 코드가 아닙니다.\n\n\n\n")
        
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
        
        thread = threading.Thread(target=fetch_album_info, args=(url, text_area, delete_url_after_download, url_entry, delay))
        thread.start()
    else:
        text_area.insert(tk.END, "[안내] 잘못된 URL입니다. 올바른 URL을 입력하십시오.\n\n")
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 문서", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_area.get('1.0', tk.END))
            messagebox.showinfo("알림", "파일이 성공적으로 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("알림", f"파일을 저장하는 중 오류가 발생했습니다: {e}")

def exit_program():
    root.destroy()



def show_help():
    help_text = """[안내]
음원 스트리밍 사이트 지니뮤직(Genie Music)에 등록된 가수의 모든 앨범 정보를 한 번에 크롤링(Crawling) 합니다.



[체크 박스]
작업 후 아티스트 앨범 URL 값 초기화:
ㄴ 비 활성화(기본값): 입력 값 유지
ㄴ 활성화: 모든 작업이 끝나면 입력 값 삭제



[버튼]
앨범 정보 가져오기: 지니뮤직 아티스트 앨범 페이지에 있는 모든 정보를 가지고 옴
log Clear: 화면 하단 Log 값 모두 삭제
"""
    messagebox.showinfo("도움말(Help)", help_text)

def show_program_about():
    show_program_about_text = """Genie Music Artist Album Crawler (Version 1.0)

Created by (Github) IZH318 in 2024.

이 소프트웨어의 사용으로 인해 발생하는 모든 문제에 대한 책임은 사용자 본인에게 있습니다.
(This software's usage is solely the responsibility of the user for any issues that may arise.)
"""
    messagebox.showinfo("정보(About)", show_program_about_text)



def select_all():
    text_area.tag_add("sel", "1.0", "end")

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def delete():
    text_area.event_generate("<<Clear>>")

def clear_result_text():
    text_area.delete('1.0', tk.END)

def insert_into_text_area(text_area, message):
    text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
    text_area.insert(tk.END, message + "\n")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)



# GUI 생성
root = tk.Tk()
root.title("Genie Music Artist Album Crawler")

# 창 크기 설정
window_width = 854
window_height = 480

# 창 크기 조정 설정
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)

# 화면의 가로 및 세로 크기 구하기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 창을 화면 가운데에 위치시키기
position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")  # 창의 위치 설정



# 메뉴 생성
menubar = Menu(root)

# 파일 메뉴
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="저장(Save)", command=save_to_file)
file_menu.add_separator()  # 구분선 추가
file_menu.add_command(label="강제 종료(Force Exit)", command=exit_program)
menubar.add_cascade(label="파일(File)", menu=file_menu)

# 도움말 메뉴
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="도움말 보기(Help)", command=show_help)
help_menu.add_separator()  # 구분선 추가
help_menu.add_command(label="정보(About)", command=show_program_about)
menubar.add_cascade(label="도움말(Help)", menu=help_menu)

# 메뉴 설정
root.config(menu=menubar)

# 첫 번째 줄: 레이블, 입력 필드
url_label = tk.Label(root, text="지니뮤직 아티스트 앨범 URL 입력:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=70)
url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

# 두 번째 줄: 체크 박스, 버튼
delete_url_after_download = BooleanVar()
checkbox = tk.Checkbutton(root, text="작업 후 아티스트 앨범 URL 값 초기화", variable=delete_url_after_download)
checkbox.grid(row=1, column=0, padx=10, pady=10, sticky='w')

fetch_button = tk.Button(root, text="앨범 정보 가져오기", command=lambda: start_fetching(url_entry, text_area, delete_url_after_download))
fetch_button.grid(row=1, column=1, padx=10, pady=10)

button_clear = Button(root, text="log Clear", command=clear_result_text)
button_clear.grid(row=1, column=2, padx=10, pady=10, sticky='e')

text_area = Text(root, wrap=tk.WORD, height=20)
text_area.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# 세 번째 줄: 결과 텍스트 위젯, 스크롤바 연결
scrollbar = Scrollbar(root, command=text_area.yview)
scrollbar.grid(row=2, column=3, sticky='ns')
text_area.config(yscrollcommand=scrollbar.set)

# 오른쪽 클릭 컨텍스트 메뉴
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="모두 선택(Select All)", command=select_all)
context_menu.add_separator()  # 구분선 추가
context_menu.add_command(label="잘라내기(Cut)", command=cut)
context_menu.add_command(label="복사(Copy)", command=copy)
context_menu.add_command(label="붙여넣기(Paste)", command=paste)
context_menu.add_separator()
context_menu.add_command(label="삭제(Delete)", command=delete)

# 마우스 오른쪽 클릭 이벤트 바인딩
text_area.bind("<Button-3>", show_context_menu)



# GUI 실행
root.mainloop()
