# Genre Surf User Interface

## 음악 장르 분류 및 곡 추천 웹 프로젝트 화면

### 🚀 프로젝트 설명

이 프로젝트는 음악 장르 분류를 통한 곡 추천 웹 프로젝트입니다.

이 폴더는 프로젝트의 User Interface를 담고 있습니다.

사용자로부터 오디오 파일을 입력 받고, 사용자가 해당 오디오 파일에 대해 장르 분류를 요청할 시에 서버에게 장르 분류 API를 요청하게 됩니다.

서버에서 장르 분류 API에 대한 응답으로 장르명을 전달하면 클라이언트는 해당 장르와 관련된 재생목록 생성 및 재생 API를 호출할 수 있습니다.

재생목록의 재생이 모두 끝나면 클라이언트의 콘솔창에서 총 몇시간(서버에서 24시간 이상으로 맞춤) 재생하였는지 출력이 됩니다.

### ⚠️ 프로젝트 시작 전!

```
npm install
```

을 통해 필요한 모듈을 설치해주세요.

```
npm start
```

모듈이 모두 설치 되었으면 위 명령어를 통해 웹프로젝트의 User Interface를 `http://localhost:3000/`에서 띄울 수 있게 됩니다.
