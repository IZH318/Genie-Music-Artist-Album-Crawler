# Genie-Music-Artist-Album-Crawler
### 지니뮤직에 등록 되어 있는 특정 아티스트의 앨범 정보(* 정규앨범, 싱글/EP, 기타앨범, 참여앨범 등을 포함 한 전체앨범 정보)를 한 번에 크롤링 하는 Python Script 입니다. <BR>

<BR> <BR> <BR>



## 🔍 주요 기능
![_2024_07_14_10_14_37_543-cut-merged-1720919890769-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/5627c973-493a-4ec3-a0ed-9f0e34d90638) <BR> <BR>
■ 아티스트의 앨범 정보 URL에서 특정 앨범 유형의 앨범 정보가 크롤링 됩니다. <BR>

<BR> <BR> <BR>



## 🛠 업데이트 내역
### ※ v1.0.0 (2024-07-13) <BR>
지니 뮤직에 등록되어 있는 특정 아티스트의 앨범 정보 전체 크롤링 <BR>

### ※ v1.1.0 (2024-07-14) <BR>
`앨범 정보 가져오기`버튼 클릭 후 대기시간 조절(5초 -> 3초)  <BR>
지니 뮤직에 등록되어 있는 특정 아티스트의 특정 앨범 유형만 선택하여 크롤링 하는 기능 구현 <BR>

<BR> <BR> <BR>



## 💾 다운로드
### ※ 본 Repositories Releases로 이동하여 다운로드 하십시오. <BR> <BR>
### ※ 본 도구를 사용할 때 필요한 모든 파일들은 zip 파일에 포함되어 있습니다. <BR>
***본 Repositories Releases에 제공 된 .zip 파일을 사용하려는 경우 개별 다운로드 과정을 생략해도 되며, 제공 된 설치 파일들을 신뢰하지 않을 경우 아래 링크를 통해 개별 다운로드 하시기 바랍니다.** <BR>

| Program                                | URL                                                | 필수여부 | 비고                                                                                           |
|----------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------------------------------------|
| `Python 3.8.0`            | [Download](https://www.python.org/downloads/release/python-390/)   | 필수     | ◼ Python Script 동작, 파이썬 3.8.0 버전 또는 그 이상 사용 가능 |
| `Chrome`            | [Download](https://www.google.com/chrome/)   | 필수     | ◼ 크롤링 전용 웹 브라우저 |
| `Chrome Driver`            | [Download](https://googlechromelabs.github.io/chrome-for-testing/)   | 필수     | ◼ 추가 플러그인 |

<BR> <BR> <BR>



## ❗ 주의 사항 ❗
### ※ 모든 내용은 2024-07-13 기준입니다.
### ※ 미처 발견하지 못한 오류가 있을 수 있습니다.

<BR> <BR> <BR>



## ⏩ 설치 방법 (초급자용 설명서)
01. Python 공식 홈페이지에서 설치 파일을 다운로드 받거나 Repositories에서 다운로드 받은 zip 파일을 적절한 위치에 압축 해제 한 후 Python 설치 파일을 실행 합니다. <BR> <BR>
![2024-07-13 08 21 14](https://github.com/user-attachments/assets/e40b40bc-6e9e-4c28-82b9-efa8a21d8ecd) <BR> <BR>
or <BR> <BR>
![2024-07-13 08 21 37](https://github.com/user-attachments/assets/34b0e99e-a30a-4e57-843b-ed0c2a4dc64e) <BR> <BR>
![2024-07-13 08 21 50](https://github.com/user-attachments/assets/bd617bbb-e83d-43ce-a1f6-0214ecfaf83e) <BR>
<BR> <BR> <BR>



2. Python을 설치합니다. <BR> <BR>
![2024-07-13 08 22 02](https://github.com/user-attachments/assets/287325f6-0b86-4b00-a981-0e9ddb701755) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
![2024-07-13 08 22 15](https://github.com/user-attachments/assets/40d7cdd1-0b70-44a8-ab73-4c2b6b2bcd4a) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR>
<BR> <BR> <BR>



3. Chrome 설치 합니다. <BR> <BR>
![2024-07-13 08 22 38](https://github.com/user-attachments/assets/e01a086d-8d74-472b-8cf7-bca2ac655999) <BR>
<BR> <BR> <BR>



4. Chrome Driver 다운로드 받습니다. <BR> <BR>
![2024-07-13 08 22 54](https://github.com/user-attachments/assets/636d9e9d-c8e7-4e58-bdcf-57b2fa0cc932) <BR>
(📌 사용 하는 PC 환경에 맞게 다운로드, Windows 환경 사용자 이면서 본 Repositories Releases에 제공 된 .zip 파일 다운로드 받았다면 이 단계 생략 가능) <BR> <BR>
**[ ※ 주의 ] 압축 해제 후 반드시 Script 파일과 동일 디렉터리 또는 하위 디렉터리에 배치 (지정된 하위 디렉터리 폴더 명은 없기 때문에 폴더 이름 상관 없이 인식 가능)** <BR>
<BR> <BR> <BR>



5. 모두 설치가 끝났다면 키보드 `Win + R` 또는 `시작 -> 검색`란에 `cmd`를 입력하여 cmd를 실행합니다. <BR> <BR>
![2024-07-12 04 37 07](https://github.com/user-attachments/assets/c403930d-a1b3-469f-b0ee-3811e7d68b8e) <BR> <BR> <BR> <BR>
cmd가 실행되었다면 아래 내용을 참고하여 필요한 패키지를 업데이트(선택) 또는 설치 합니다. <BR> <BR>
5-1. **(선택사항, 생략가능) Python Package Update** <BR> <BR>
(* 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip` <BR>
or <BR>
`python -m pip install --upgrade pip` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install --upgrade pip --user` <BR>
or <BR>
`python -m pip install --upgrade pip --user` <BR>
<BR> <BR> <BR>
5-2. **(필수) Package 설치** <BR> <BR>
`pip install selenium beautifulsoup4` <BR>
or <BR>
`python -m pip install selenium beautifulsoup4` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install selenium beautifulsoup4 --user` <BR>
or <BR>
`python -m pip install selenium beautifulsoup4 --user` <BR>
<BR> <BR> <BR>



## ⏩ 사용 방법
01. `Genie Music Artist Album Crawler.py`를 실행합니다. <BR> <BR>
![2024-07-14 10 21 45](https://github.com/user-attachments/assets/18d8ada2-f0f7-464b-a153-6de50f98430e) <BR>
<BR> <BR> <BR>



2. GUI 상단 `지니뮤직 아티스트 앨범 URL 입력:` 란에 URL 입력 후 `앨범 종류 가져오기`버튼을 클릭합니다. <BR> <BR>
(📌 `https://www.genie.co.kr/detail/artistAlbum?xxnm=`로 시작하는 문자열만 처리 됩니다.) <BR>
<BR> <BR> <BR>



3. 앨범 종류가 정상적으로 반환 되었다면 원하는 앨범 종류를 선택 후 `앨범 정보 가져오기`버튼을 누르거나, `작업 후 아티스트 앨범 URL 값 초기화`체크 박스 기능을 활성화 하고 `앨범 정보 가져오기`버튼을 누릅니다. <BR> <BR>
**[ ※ 주의 ] 크롤링 중인 웹 브라우저를 최소화 또는 창 위치 이동, 창 크기 조절 하는 것은 괜찮으나, 웹 브라우저 화면에 보이는 항목들을 클릭하는 등의 작업은 금지** <BR> <BR> <BR> <BR>
![_2024_07_13_08_17_31_527-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/64f1a5db-a44e-49c4-907e-a75e6be2cebd) <BR>
(📌 `앨범 정보 가져오기`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_13_08_18_04_886-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/500c1182-5169-49e4-b98a-296b9d3c459b) <BR>
(📌 `작업 후 아티스트 앨범 URL 값 초기화` 체크 박스 활성화 후 `앨범 정보 가져오기`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_13_08_18_43_407-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/073736a8-46cb-4793-b2c4-91bb6cc379cd) <BR>
(📌 메뉴 `파일(File) - 저장(Save)`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_13_08_18_50_709-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/7773e39c-3598-4038-a8ee-f578326f6eb6) <BR>
(📌 `log Clear`버튼 클릭) <BR>
<BR> <BR> <BR>



## ⚙ 코드 수정 (선택)
### ※ 이 작업은 Python 언어로 작성 된 Script의 내용을 이해하고 응용할 수 있는 분들께 추천드리는 작업입니다. <BR><BR>

### ❗ 필수 작업 ❗ <BR>
![Genie Music Artist Album Crawler 읽기 전용 해제 설명](https://github.com/user-attachments/assets/7827d33f-c941-45fd-bd24-150e17f4ae7f) <BR>
(📌 Repositories Releases에 제공 된 .zip 파일을 다운 받았는 경우에만 해당) <BR> <BR>
제공 된 Python Script를 수정하고자 하는 파일 선택 후 `마우스 우클릭 -> 속성 -> 일반 -> 특성` 항목 중 `읽기 전용(R)`상태 해제 후 확인 <BR>
<BR> <BR> <BR>



01. 지연 시간 변경 <BR> <BR>
`앨범 종류 가져오기` 버튼 클릭 시: <BR>
54번째 줄 `delay = 1` 수정 (* 기본값 = 1, 초 단위로 입력) <BR> <BR>
`앨범 정보 가져오기` 버튼 클릭 시: <BR>
176번째 줄 `delay = 3` 수정 (* 기본값 = 3, 초 단위로 입력) <BR>
<BR> <BR> <BR>



02. 초기 안내 문구 유지 <BR> <BR>
`앨범 종류 가져오기` 버튼 클릭 시: <BR>
47번째 줄 `clear_result_text()` 주석 처리 또는 삭제 <BR> <BR>
`앨범 정보 가져오기` 버튼 클릭 시: <BR>
167번째 줄 `clear_result_text()` 주석 처리 또는 삭제 <BR>
<BR> <BR> <BR>



03. 각 버튼 별 웹 사이트 표시 여부 설정 <BR> <BR>
`앨범 종류 가져오기` 버튼 클릭 시 웹 사이트 표시 안 함 (* 기본값): <BR>
80번째 줄 `options.add_argument('--headless')` 그대로 유지<BR> <BR>
`앨범 종류 가져오기` 버튼 클릭 시 웹 사이트 표시: <BR>
80번째 줄 `options.add_argument('--headless')` 주석 처리 또는 삭제<BR>
<BR> <BR> <BR>
`앨범 정보 가져오기` 버튼 클릭 시 웹 사이트 표시 안 함: <BR>
212번째 줄 `options.add_argument('--headless')` 주석 처리 또는 삭제 <BR> <BR>
`앨범 정보 가져오기` 버튼 클릭 시 웹 사이트 표시 (* 기본값): <BR>
212번째 줄 `options.add_argument('--headless')` 그대로 유지 <BR>
<BR> <BR> <BR>
