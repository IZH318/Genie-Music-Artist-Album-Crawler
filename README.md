# Genie-Music-Artist-Album-Crawler
### 지니뮤직에 등록 되어 있는 아티스트의 앨범 정보(정규앨범, 싱글/EP, 기타앨범, 참여앨범 등을 포함 한 전체앨범 정보)를 한 번에 크롤링 하는 Python Script 입니다. <BR>

<BR> <BR> <BR>



## 🔍 주요 기능
![_2024_07_13_06_04_44_540-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/33272896-67ff-466c-afb9-08c141ce591d) <BR> <BR>
■ 원하는 아티스트의 앨범 정보란으로 이동 후 URL을 복사하여 붙여넣으면 자동으로 전체앨범 정보가 크롤링 됩니다. <BR>

<BR> <BR> <BR>



## 💾 다운로드
### ※ 본 Repositories Releases로 이동하여 다운로드 하십시오. <br><br>
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
![2024-07-12 04 26 46](https://github.com/user-attachments/assets/7c88f4e1-3414-4268-8a14-cee13ac12233) <BR> <BR>
or <BR> <BR>
![2024-07-12 04 26 55](https://github.com/user-attachments/assets/56d9006d-b28d-46f3-bd2d-9ffe383ead12) <BR> <BR>
![2024-07-12 04 47 21](https://github.com/user-attachments/assets/b9242a42-c989-449f-974e-22a2ece46fd3)

<BR> <BR> <BR>



2. Python을 설치합니다. <BR> <BR>
![2024-07-12 04 27 14](https://github.com/user-attachments/assets/6cb0b356-e12f-4714-adde-30cd9850ec81) <BR>
**[ ※ 주의 ] Python 설치 시 Add python.exe to PATH 에 반드시 체크 후 Install Now 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 또는 제거 후 재 설치) <BR> <BR>
![2024-07-12 04 27 26](https://github.com/user-attachments/assets/050db49e-0478-4f0f-9ce8-44fdef0cadc9) <BR>
**[ ※ 주의 ] 설치 후 Disable path length limit 기능을 사용할 수 있도록 반드시 클릭** <BR>
(📌 미처 누르지 못했다면 설치 파일 다시 실행 후 작업 또는 제거 후 재 설치) <BR> <BR> <BR> <BR>


3. 모두 설치가 끝났다면 키보드 `Win + R` 또는 `시작 -> 검색`란에 `cmd`를 입력하여 cmd를 실행합니다. <BR> <BR>
![2024-07-12 04 37 07](https://github.com/user-attachments/assets/c403930d-a1b3-469f-b0ee-3811e7d68b8e) <BR> <BR> <BR> <BR>



4. cmd가 실행되었다면 아래 내용을 참고하여 필요한 패키지를 업데이트(선택) 또는 설치 합니다. <BR> <BR>
4-1. **(선택사항, 생략가능) Python Package Update** <BR> <BR>
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
4-2. **(필수) rsack Package 설치** <BR> <BR>
`pip install selenium beautifulsoup4` <BR>
or <BR>
`python -m pip install selenium beautifulsoup4` <BR> <BR>
**[ ※ 주의 ] 만약 위 명령어 사용 중 ERROR: Could not install packages due to an EnvironmentError: [WinError 5] 액세스가 거부되었습니다: (생략) Consider using the `--user` option or check the permissions. 과 같은 오류가 나왔다면 끝에 `--user`를 붙여서 입력** <BR> <BR>
(* 권한 오류 발생시 두 코드 중 하나 선택) <BR>
`pip install selenium beautifulsoup4 --user` <BR>
or <BR>
`python -m pip install selenium beautifulsoup4 --user` <BR>
<BR> <BR> <BR>



5. (필수) Chrome Driver 다운로드 <BR> <BR>
5-1. 확장자 숨김 처리 해제 <BR> <BR>
![확장자 표시 설명](https://github.com/user-attachments/assets/ec81c43a-2c51-48c3-bcfe-d681cedd0832) <BR>
(📌 **[ ※ 필수 ]** 확장자가 숨김 처리 된 상태인 경우 반드시 위 스크린 샷 참고하여 확장자 표시 상태로 작업 ) <BR> <BR> <BR> <BR>
5-2. PC 계정 폴더로 이동 후 rsack_settings.ini 생성 <BR> <BR>
![2024-07-12 04 52 57](https://github.com/user-attachments/assets/e2db3ffd-b622-42f9-bb9a-c483d1d4a6bc) <BR> <BR>
![2024-07-12 04 51 28](https://github.com/user-attachments/assets/751b9658-0b1d-4848-8c59-e7a4604b6ce0) <BR>
(📌 PC 계정 명이 User 인 경우 `C:\Users\User` 로 이동 후 rsack_settings.ini 생성 ) <BR> <BR> <BR> <BR>
5-3. rsack_settings.ini 내용 작성 <BR> <BR>
**[ ※ 주의 ] 반드시 https://github.com/Slyyxp/rsack/blob/master/rsack_settings.ini.example 전체 코드 기반으로 작업** <BR> <BR>
![2024-07-12 05 06 58](https://github.com/user-attachments/assets/8d28ca3c-4583-4014-97b5-ab7b6e4f9d53) <BR>
(📌 위 링크 이동 후 전체 본문 복사 후 붙여넣고 proxy 설정은 반드시 `proxy = false`로 수정) <BR> <BR>
![2024-07-12 04 28 25](https://github.com/user-attachments/assets/19c098fe-7a65-4723-a076-68e242de3400) <BR>
(📌 위 예시는 아래와 같음 (* 아래 내용은 단순히 참고용으로만 사용) ) <BR> <BR>
![2024-07-12 05 19 06](https://github.com/user-attachments/assets/8091ade2-cf9b-44ae-aa41-8a7e8b71e280) <BR>
(📌 만약, 한글이 포함 된 경로를 사용하거나, 주석을 포함하여 저장하고 싶은 경우 `UTF-8` 인코딩이 아닌 `ANSI` 인코딩으로 설정 변경 후 저장) ) <BR>
<BR> <BR> <BR>



## ⏩ 사용 방법
01. `Genie Music Artist Album Crawler.py`를 실행합니다. <BR> <BR>
![2024-07-12 05 33 07](https://github.com/user-attachments/assets/d83eabf5-525c-4a04-be21-80dda4d39278) <BR> <BR> <BR> <BR>



2. `Genie Music Artist Album Crawler.py` 상단 `지니뮤직 아티스트 앨범 URL 입력:` 란에 URL을 입력합니다. <BR> <BR>
![2024-07-12 05 34 53](https://github.com/user-attachments/assets/763fb190-38df-42c3-8e9a-58c204866855) <BR>
(📌 `https://www.genie.co.kr/detail/artistAlbum?xxnm=`로 시작하는 문자열만 처리 됩니다.) <BR> <BR> <BR> <BR>



3. `지니뮤직 아티스트 앨범 URL`을 입력했다면 `앨범 정보 가져오기`버튼을 누르거나, 체크 박스 기능을 활성화 하고 `앨범 정보 가져오기`버튼을 누릅니다. <BR> <BR>
![_2024_07_12_05_28_42_749-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/4ecfe8d3-7b4c-4cae-8544-3299c886e56e) <BR>
(📌 `앨범 정보 가져오기`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_29_04_620-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/e78a3c4f-f3af-4092-a949-39cf992b3845) <BR>
(📌 `작업 후 아티스트 앨범 URL 값 초기화` 체크 박스 활성화 후 `앨범 정보 가져오기`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_28_49_89-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/822b7f8a-fd2c-40bb-9a44-7728223f919a) <BR>
(📌 `log Clear`버튼 클릭) <BR> <BR> <BR> <BR>
![_2024_07_12_05_28_49_89-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/822b7f8a-fd2c-40bb-9a44-7728223f919a) <BR>
(📌 메뉴 `파일(File) - 저장(Save)`버튼 클릭) <BR> <BR> <BR> <BR>
<BR> <BR> <BR>



## ⚙ 코드 수정 (선택)
### ※ 이 작업은 Python 언어로 작성 된 Script의 내용을 이해하고 응용할 수 있는 분들께 추천드리는 작업입니다. <BR><BR>

### ❗ 필수 작업 ❗ <BR>
![rsack GUI Manager 읽기 전용 해제 설명](https://github.com/user-attachments/assets/efcfd986-0229-4a62-9a44-909bd5f79854) <BR>
(📌 Repositories Releases에 제공 된 .zip 파일을 다운 받았는 경우에만 해당) <BR>
제공 된 Python Script를 수정하고자 하는 파일 선택 후 `마우스 우클릭 -> 속성 -> 일반 -> 특성` 항목 중 `읽기 전용(R)`상태 해제 후 확인 <BR>
<BR> <BR> <BR>
