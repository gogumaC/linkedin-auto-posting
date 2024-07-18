# linkedin-auto-posting

## version3
![image](https://github.com/user-attachments/assets/03feb367-02db-46bb-9c7e-69681e51d2f1)

- 24.07.16
- 기존 클라우드 서비스를 활용한 부분을 도커 컨테이너로 이전
- 도커 컴포즈를 활용해서 관리가 편해짐
- 개인 컴퓨터에서 동작시켜서 비용 감소

<br>

## version2
![linkedin-auto-posting drawio (2)](https://github.com/gogumaC/linkedin-auto-posting/assets/59639035/9b68f3f3-cdd4-4e8d-86c0-28cb5ecdc287)

- 애저를 활용해서 리눅스 서버에서 시스템 운영
- 장점은 기능의 자유도가 높다는점
- 단점은 지속적 비용 발생

<br>

## version1

- github action을 통해 포스팅 관련 커밋 푸시가 발생하면 Make(자동화 플랫폼)에 요청하여 링크드인에 포스팅
- 장점은 신경쓸게 없어서 편함
- 단점은 자유도가 매우 낮다는점. Make에서 api업데이트를 안해주면 해줄때까지 기다려야 함
