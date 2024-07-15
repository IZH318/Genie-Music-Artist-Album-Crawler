import os  # 운영 체제 관련 기능을 사용하기 위한 모듈
import re  # 정규 표현식을 사용하기 위한 모듈
import time  # 시간 관련 기능을 사용하기 위한 모듈
import threading  # 병렬 처리를 위한 모듈

# Selenium 관련 모듈
from selenium import webdriver  # 웹 브라우저를 제어하기 위한 모듈
from selenium.webdriver.chrome.service import Service  # Chrome 드라이버 서비스 설정을 위한 모듈
from selenium.webdriver.chrome.options import Options  # Chrome 브라우저 옵션 설정을 위한 모듈
from selenium.webdriver.common.by import By  # 웹 요소를 검색하기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait  # 웹 페이지가 로드될 때까지 대기하기 위한 모듈
from selenium.webdriver.support import expected_conditions as EC  # 조건이 충족될 때까지 대기하기 위한 모듈
from selenium.webdriver.common.action_chains import ActionChains  # 웹 요소에 대한 마우스 및 키보드 동작을 시뮬레이션하기 위한 모듈

# BeautifulSoup 및 GUI 관련 모듈
from bs4 import BeautifulSoup  # HTML 및 XML 문서를 구문 분석하기 위한 모듈
import tkinter as tk  # GUI를 만들기 위한 모듈
from tkinter import Menu, Button, Text, Scrollbar, BooleanVar, messagebox, filedialog, Checkbutton  # GUI 구성 요소를 사용하기 위한 모듈



# 체크 박스 상태를 저장할 리스트
checkbox_vars = []



def find_chromedriver():
    # 현재 스크립트가 위치한 디렉터리 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 현재 디렉터리 및 하위 디렉터리에서 chromedriver.exe 파일을 찾기
    for root, dirs, files in os.walk(current_dir):
        if 'chromedriver.exe' in files:
            return os.path.join(root, 'chromedriver.exe')
    
    # 찾지 못한 경우 None 반환
    return None



# 앨범 종류 가져오기
def start_fetching_album_types():
    url = url_entry.get()
    
    if url.startswith('https://www.genie.co.kr/detail/artistAlbum?xxnm='):
        # text_area 초기화
        clear_result_text()
        
        url_entry.config(state=tk.DISABLED)
        fetch_album_types_button.config(state=tk.DISABLED)
        disable_frame(checkbox_frame)

        # 지연 시간 설정 (초 단위)
        delay = 1
        
        text_area.insert(tk.END, f"\n [알림] 모든 앨범 종류를 불러오고 있습니다. 작업이 끝날 때까지 잠시 기다리십시오.\n\n", 'info')
        text_area.tag_configure('info', foreground='black', background='yellow', font=('Arial', 12, 'bold'))

        text_area.insert(tk.END, f"\n")
        
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
        
        # 알림 메시지가 출력되고 나서 지연 시간 후에 앨범 종류를 불러오는 함수 호출
        root.after(delay * 1000, fetch_album_types, url, text_area, fetch_button)
        
    else:
        text_area.insert(tk.END, "\n[안내] 잘못된 URL입니다. 올바른 URL을 입력하십시오.\n\n")
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동



def fetch_album_types(url, text_area, fetch_button):
    chrome_driver_path = find_chromedriver()

    if not chrome_driver_path:
        text_area.insert(tk.END, "\n[경고] chromedriver.exe를 찾을 수 없습니다.\n")
        return

    options = Options()
    options.add_argument('--headless')  # headless 모드(* 웹 브라우저 창 가림) 설정
    options.add_argument('--start-maximized')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    try:
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.this-type')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        album_types_div = soup.find('div', class_='this-type')

        if album_types_div:
            ul = album_types_div.find('ul')
            if ul:
                # 기존 체크박스 제거
                for widget in checkbox_frame.winfo_children():
                    widget.destroy()

                checkbox_vars.clear()  # 기존 체크박스 변수 초기화
                
                # 모든 <li> 반환
                lis = ul.find_all('li')
                
                for index, li in enumerate(lis):
                    album_type = li.get_text(strip=True)
                    checkbox_var = BooleanVar()
                    checkbox_vars.append(checkbox_var)  # 변수 저장
                    row = 1 + (index // 5)
                    column = index % 5
                    checkbox = tk.Checkbutton(checkbox_frame, text=album_type, variable=checkbox_var)
                    checkbox.grid(row=row, column=column, padx=5, pady=5, sticky='w')
                    
                    # 첫 번째 체크 박스는 따로 관리하여 선택되면 나머지 체크 박스들을 해제
                    if index == 0:
                        checkbox_var.trace_add('write', lambda *args, checkbox_var=checkbox_var: handle_first_checkbox(checkbox_var))
                    else:
                        checkbox_var.trace_add('write', lambda *args, checkbox_var=checkbox_var: handle_other_checkboxes(checkbox_var))

            else:
                text_area.insert(tk.END, "\n[앨범 종류를 찾을 수 없습니다.]\n")
        else:
            text_area.insert(tk.END, "\n[앨범 종류를 찾을 수 없습니다.]\n")

        # 체크 박스 상태에 따라 fetch_button 활성화 여부 결정
        check_checkbox_state()

    except Exception as e:
        text_area.insert(tk.END, f"\n[앨범 종류를 불러오는 중 오류 발생: {e}\n")
    
    finally:
        driver.quit()
        
        # text_area 초기화
        clear_result_text()
        
        url_entry.config(state=tk.NORMAL)
        fetch_album_types_button.config(state=tk.NORMAL)
        enable_frame(checkbox_frame)



def handle_first_checkbox(checkbox_var):
    if checkbox_var.get():
        for var in checkbox_vars[1:]:
            var.set(False)
    check_checkbox_state()



def handle_other_checkboxes(checkbox_var):
    if checkbox_var.get():
        checkbox_vars[0].set(False)
    check_checkbox_state()



def check_checkbox_state():
    all_unchecked = all(not var.get() for var in checkbox_vars)
    fetch_button.config(state=tk.NORMAL if not all_unchecked else tk.DISABLED)



# 앨범 정보 가져오기
def start_fetching(url_entry, text_area, delete_url_after_download):
    url = url_entry.get()
    if url.startswith('https://www.genie.co.kr/detail/artistAlbum?xxnm='):
        clear_result_text()
        
        # 앨범 정보 가져오기 버튼 비활성화
        url_entry.config(state=tk.DISABLED)
        fetch_album_types_button.config(state=tk.DISABLED)
        disable_frame(checkbox_frame)
        fetch_button.config(state=tk.DISABLED)

        # 지연 시간 설정 (초 단위)
        delay = 3
        
        text_area.insert(tk.END, f"\n [알림] {delay}초 후 작업이 진행 됩니다.\n\n", 'info')
        text_area.tag_configure('info', foreground='black', background='yellow', font=('Arial', 12, 'bold'))

        text_area.insert(tk.END, f"\n\n")
        
        text_area.insert(tk.END, "\n [경고] 자동화 작업이 진행되는 동안 웹 브라우저 내 요소들을 임의로 조작하지 마십시오.\n\n", 'warning')
        text_area.tag_configure('warning', foreground='white', background='red', font=('Arial', 12, 'bold'))

        text_area.insert(tk.END, f"\n")

        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
        
        thread = threading.Thread(target=fetch_album_info, args=(url, text_area, delete_url_after_download, checkbox_vars, delay))
        thread.start()
    else:
        text_area.insert(tk.END, "\n[안내] 잘못된 URL입니다. 올바른 URL을 입력하십시오.\n\n")
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동



def fetch_album_info(url, text_area, delete_url_after_download, checkboxes, delay):
    chrome_driver_path = find_chromedriver()
    
    if not chrome_driver_path:
        text_area.insert(tk.END, "\n[경고] chromedriver.exe를 찾을 수 없습니다.\n")
        
        url_entry.config(state=tk.NORMAL)
        fetch_button.config(state=tk.NORMAL)
        button_clear.config(state=tk.NORMAL)
            
        text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
        return
    
    options = Options()
    # options.add_argument('--headless')  # headless 모드(* 웹 브라우저 창 가림) 설정
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

        for checkbox in checkboxes:
            if checkbox.get():
                # 체크 박스 인덱스 추출
                index = checkboxes.index(checkbox) + 1
                
                # 해당 체크 박스에 해당하는 <li> 클릭
                li_element = driver.find_element(By.XPATH, f'//div[@class="this-type"]/h3[text()="앨범 종류"]/following-sibling::ul[1]/li[{index}]')
                li_element.click()

                while True:
                    # 1초 동안 대기 (* 웹 페이지에서 데이터를 불러오는 시간 보다 a.next 동작이 빠를 경우 대비)
                    time.sleep(1)
                    
                    try:
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.list-album')))
                        
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        
                        albums = soup.select('li.list-album')
                        
                        if not albums:
                            text_area.insert(tk.END, f"\n[안내] 페이지에서 앨범을 찾을 수 없습니다.")
                            text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                            continue

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
                                next_button.click()
                                time.sleep(2)
                        except Exception as e:
                            text_area.insert(tk.END, f"\n[경고] 다음 페이지로 이동하는 버튼을 찾을 수 없거나 다른 문제가 발생하였습니다.: {e}\n")
                            text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                            continue

                    except Exception as e:
                        text_area.insert(tk.END, f"\n[알림] 예외 발생: {e}\n\n\n")
                        try:
                            alert = driver.switch_to.alert
                            alert_text = alert.text
                            alert.accept()
                            text_area.insert(tk.END, f"\n[안내] 알림이 수락되었습니다: {alert_text}\n\n")
                            if "마지막 페이지입니다" in alert_text:
                                text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                                break
                        except Exception as alert_exception:
                            text_area.insert(tk.END, f"\n[안내] Failed to handle alert: {alert_exception}\n\n\n")
                            text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
                        break

        if album_info_list:
            # text_area 초기화
            clear_result_text()
            
            text_area.insert(tk.END, f"\n [알림] 모든 작업이 정상적으로 처리되었습니다.\n\n", 'info')
            text_area.tag_configure('info', foreground='black', background='yellow', font=('Arial', 12, 'bold'))
            
            text_area.insert(tk.END, f"\n\n\n===== [{artist_name}] Album Information =====\n\n")
            
            for album_info in album_info_list:
                text_area.insert(tk.END, '-' * 40 + '\n')
                text_area.insert(tk.END, f"Title: {album_info['Title']}\n")
                text_area.insert(tk.END, f"Release Date: {album_info['Release Date']}\n")
                text_area.insert(tk.END, f"Track Count: {album_info['Track Count']}\n")
                text_area.insert(tk.END, f"Album Info: {album_info['fnViewAlbumLayer']}\n")
                text_area.insert(tk.END, f"\n[Album URL]\nhttps://www.genie.co.kr/detail/albumInfo?axnm={album_info['fnViewAlbumLayer']}\n")
                text_area.insert(tk.END, '-' * 40 + '\n\n')

        else:
            text_area.insert(tk.END, "\n[안내] 앨범 정보를 찾을 수 없습니다.\n\n")
            text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
    
    finally:
        # 작업이 끝난 후에 버튼 다시 활성화
        url_entry.config(state=tk.NORMAL)
        fetch_album_types_button.config(state=tk.NORMAL)
        enable_frame(checkbox_frame)
        
        if delete_url_after_download.get():
            url_entry.delete(0, tk.END)
            
        driver.quit()



def split_desc(desc):
    parts = desc.split('|')
    release_date = parts[0].strip() if len(parts) > 0 else 'N/A'
    track_count = parts[2].strip() if len(parts) > 2 else 'N/A'
    return release_date, track_count



# 프레임 안에 있는 모든 위젯을 비활성화하는 함수
def disable_frame(frame):
    for child in frame.winfo_children():
        child.configure(state='disabled')



# 프레임 안에 있는 모든 위젯을 활성화하는 함수
def enable_frame(frame):
    for child in frame.winfo_children():
        child.configure(state='normal')



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
앨범 종류 가져오기: 지니뮤직 아티스트 앨범 페이지에 있는 모든 앨범 종류를 가지고 옴
앨범 정보 가져오기: 지니뮤직 아티스트 앨범 페이지에 있는 모든 앨범 정보를 가지고 옴
log Clear: 화면 하단 Log 값 모두 삭제
"""
    messagebox.showinfo("도움말(Help)", help_text)



def show_program_about():
    show_program_about_text = """Genie Music Artist Album Crawler (Version 1.1)

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
    text_area.delete('1.1', tk.END)

def insert_into_text_area(text_area, message):
    text_area.see(tk.END)  # 스크롤바를 맨 아래로 이동
    text_area.insert(tk.END, message + "\n")

def show_url_entry_context_menu(event):
    context_menu_url_entry.post(event.x_root, event.y_root)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)



# GUI 생성
root = tk.Tk()
root.title("Genie Music Artist Album Crawler")

# 창 크기 설정
window_width = 854
window_height = 480

# 창 크기 조정 설정
root.grid_rowconfigure(3, weight=1)
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

# 두 번째 줄: 앨범 종류 체크 박스
fetch_album_types_button = tk.Button(root, text="앨범 종류 가져오기", command=start_fetching_album_types)
fetch_album_types_button.grid(row=1, column=0, padx=10, pady=10)

checkbox_frame = tk.Frame(root)
checkbox_frame.grid(row=1, column=1, columnspan=2, padx=0, pady=0, sticky='ew')

# 세 번째 줄: 체크 박스, 버튼
delete_url_after_download = BooleanVar()
checkbox = tk.Checkbutton(root, text="작업 후 아티스트 앨범 URL 값 초기화", variable=delete_url_after_download)
checkbox.grid(row=2, column=0, padx=10, pady=10, sticky='w')

fetch_button = tk.Button(root, text="앨범 정보 가져오기", command=lambda: start_fetching(url_entry, text_area, delete_url_after_download), state=tk.DISABLED)
fetch_button.grid(row=2, column=1, padx=10, pady=10)

button_clear = Button(root, text="log Clear", command=clear_result_text)
button_clear.grid(row=2, column=2, padx=10, pady=10, sticky='e')

# 네 번째 줄: 결과 텍스트 위젯, 스크롤바 연결
text_area = Text(root, wrap=tk.WORD, height=20)
text_area.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

scrollbar = Scrollbar(root, command=text_area.yview)
scrollbar.grid(row=3, column=3, sticky='ns')
text_area.config(yscrollcommand=scrollbar.set)



# url_entry의 오른쪽 클릭 컨텍스트 메뉴
context_menu_url_entry = Menu(root, tearoff=0)
context_menu_url_entry.add_command(label="모두 선택(Select All)", command=lambda: url_entry.select_range(0, 'end'))
context_menu_url_entry.add_separator()  # 구분선 추가
context_menu_url_entry.add_command(label="잘라내기(Cut)", command=lambda: url_entry.event_generate("<<Cut>>"))
context_menu_url_entry.add_command(label="복사(Copy)", command=lambda: url_entry.event_generate("<<Copy>>"))
context_menu_url_entry.add_command(label="붙여넣기(Paste)", command=lambda: url_entry.event_generate("<<Paste>>"))
context_menu_url_entry.add_separator()
context_menu_url_entry.add_command(label="삭제(Delete)", command=lambda: url_entry.delete(0, 'end'))

# url_entry에 마우스 오른쪽 클릭 이벤트 바인딩
url_entry.bind("<Button-3>", show_url_entry_context_menu)



# text_area의 오른쪽 클릭 컨텍스트 메뉴
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="모두 선택(Select All)", command=select_all)
context_menu.add_separator()  # 구분선 추가
context_menu.add_command(label="잘라내기(Cut)", command=cut)
context_menu.add_command(label="복사(Copy)", command=copy)
context_menu.add_command(label="붙여넣기(Paste)", command=paste)
context_menu.add_separator()
context_menu.add_command(label="삭제(Delete)", command=delete)

# text_area에 마우스 오른쪽 클릭 이벤트 바인딩
text_area.bind("<Button-3>", show_context_menu)



# GUI 실행
root.mainloop()
