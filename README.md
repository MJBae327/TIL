# 7/12
- GUI(Graphic User Interface)

- TUI 혹은 CLI는 GUI와 반대되는 개념. 윈도우 CLI에는 CMD, powershell, bash가 있음.

- bash는 리눅스 명령어를 사용하기 때문에 명령어를 입력하기에 간편하고 편리하다는 장점이있음.

- git은 git bash를 사용하기 위해 설치. git은 CLI의 한 종류이다.


### ***기술을 왜쓸까?*** 라는 생각을 계속 해야 한다!


- ChatGPT에서 GPT는 Generative Pre-trained Transformer. 트랜스포머의 특징은 자연어 입력이 가능하다는 것이다. 딥러닝 모델이라고 생각하면 된다.

- HTML(Hyper Text Markup Language)로는 로직을 작성할 수 없으며 배치에 관여한다.

- CSS는 색깔이나 크기 조절, 꾸미는 역할을 한다.

- Javascript에는 로직이 들어간다.

- 클라이언트는 서버에 request하고 서버는 response한다.

- API: 클라이언트가 서버에게 요청하는 규칙. API를 요청하면 **Json으로 된 파일 형식**을 받을 수 있다.
---

# 7/13
- 마크다운: 프로젝트에 대한 설명을 문서화 한 것이 마크다운. 가독성과 편리성이 좋아서 사용한다.

  1. 글꼴 크기 비교하기
        # 헤더1
        ## 헤더2
        ### 헤더3
        #### 헤더4
        ##### 헤더5
        ###### 헤더6
        6까지만 되는 듯하다

  2. ordered list 적기
     1. 지금 작성하고 있는 형태가 ordered list 이다.
     2. enter를 누르면 다시 돌아가며, tab을 누르면 현재 상태와 같이 order 아래에 하위 order가 형성된다.


  3. unordered list 적기
      - 이 형태가 unordered list이고 작동방식은 ordered list와 같다.

  4. 체크 리스트 적기
       1. [ ] 개인적으로 가장 신기했던 방식이다.
       2. [ ] 저 앞에 숫자는 안 없어지는 듯하다..
       3. [x] 체크를 원하면 이런식으로 해주면 된다.

   5. 코드 블록
        -  ```python
            print("Hello World!")
            ```
   6. 링크 url 걸기

      [에듀싸피](https://edu.ssafy.com/edu/main/index.do)

   7. 이미지 걸기
        ![동바오생바오](https://contents-cdn.viewus.co.kr/image/2023/07/CP-2022-0028/image-1d336f66-0247-40e6-9e47-52964b97670c.jpeg)

   8.  글꼴
       1.  **굵은글씨1** __굵은글씨2__
       2.  *기울인글씨1* _기울인글씨2_
       3.  ***굵고기울인글씨1*** ___굵고기울인글씨2___
       4.  ~~취소선~~
       5.  나누는 선
        ---

- GIT: git은 코드의 변경 이력을 기록하고 프로젝트 협업을 위해 사용한다. 같은 파일을 동시에 작업하면 충돌이 일어날 수 있는데, 분산구조는 이런 충돌을 줄여주고 인터넷에 연결되지 않은 환경에서도 작업을 계속 할 수 있게 해준다.
- git의 3가지 영역에는 working directory, staging area, repository가 있다.
- git commit 실습
```bash
$ cd Desktop #바탕화면 보기

$ mkdir git_commit #git_commit이라는 폴더 생성

$ git config --global user.name 배민지 #커밋작성자 정보 작성

$ git config --global user.email bae1997@naver.com #커밋작성자 정보 작성

$ git config --global -l #커밋작성자 정보 확인

$ git init #새로운 git 저장소생성

$ touch a.txt #a.txt 파일 생성(로컬저장소에)

$ git add a.txt #staging area에 a.txt 파일 add

$ git status #git 상태 확인(커밋준비가 되었는가?)

$ git commit -m "커밋명" #커밋

$ git log #커밋 확인

$ rm -rf .git #나가기
```
- 참고로 한 폴더 안에 여러개의 파일이 있는 경우, 커밋을 막고 싶은 파일이 있다면 echo 파일명 >> .getignore 로 ignore 해주면 된다.
---

# 7/14
- git = local repository
- git hub = remote repository
- local -> remote: push
- remote -> local: pull, clone


- git push, pull, clone 실습 
```bash
#먼저 여러개의 파일이 있는 폴더 git_practice를 push 해보자
$ git commit -m 'first_pjt' #커밋명 first_pjt 으로 커밋

$ git log #커밋이 잘 되었는지 확인

$ git remote add 원격저장소별칭 원격저장소url #로컬 저장소에 원격 저장소 주소를 추가

$ git remote -v # 원격저장소 확인

$ git push 원격저장소별칭 +브랜치명 #push

$ git pull 원격저장소별칭 브랜치명 #pull

$ git clone 원격저장소url
#pull은 업데이트의 개념이고
#clone은 아예 새로운 프로젝트를 시작해서 선행작업에 대한 히스토리가 없을 경우 한다.
```