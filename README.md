[Kotlin - SpringBoot rbac assignment 참조]  
https://github.com/Marc416/nota-ai-assignment-RBAC

과제에대한 정보도 위 링크를 참조 부탁드립니다.

---
python version : 3.13

유저의 Role 에 따라 계정제어, 프로젝트 제어를 할 수 있습니다.  
크게 AccountRole, ProjectRole 로 나뉘어 집니다.  

코드 철학 : 누구나 보기 쉽고 빠르게 이해하고 유지보수하기 편한 소프트웨어를 만드는 것을 목표. 유지보수, 테스트, 확장에 유연하고 빠른 개발을 할 수 있게.  

객체지향 설계 5원칙 SOLID (SRP, OCP, LSP, ISP, DIP) 을 지키려 노력했습니다.

사용한 아키텍처 : 헥사고날 아키텍처(알리스테어 코클번 (Alistair Cockburn))  
-> 레이어드 아키텍처의 한계를 극복하기 위해 클린아키텍처 철학을 고수하되 각 도메인, 모듈, 기능등등의 의존성을 강하게 분리하고 제어하기 위해 나타남.   
<img width="530" alt="image" src="https://github.com/user-attachments/assets/a4196028-ae2d-401d-ab14-b34bb86f9011" />  
코드 구조  
<img width="473" alt="image" src="https://github.com/user-attachments/assets/7ef8acb8-75d1-4507-8872-a93325c1be16" />  

레이어드 아키텍처란 ?  
```
사용자가 "주문 생성" 요청을 보냄
↓
Presentation (Controller): 유저 요청 수신
↓
Application (OrderService): 유즈케이스 실행
↓
Domain (Order, PaymentPolicy 등): 비즈니스 로직 실행
↓
Infrastructure (DB, 외부 API): 저장 또는 외부 통신
```

그럼 클린아키텍처란?(로버트 C. 마틴 (Robert C. Martin))  
-> 레이어드 구조(계층간 책임분리), 밖에서 안으로 의존성을 가진다가 핵심  
<img width="544" alt="Pasted Graphic 14" src="https://github.com/user-attachments/assets/26ba0327-199d-4873-8238-a9b7e09d2ed4" />  
계좌 송금 시스템을 레이어드 아키텍처로 표현  
<img width="559" alt="계층으로 구성하기" src="https://github.com/user-attachments/assets/19b4e71c-defa-4f79-9bb0-7693f45dbbb4" />

단점  
1. 애플리케이션간의 구분을 짓는 패키지 경계가 없다.
2. 애플리케이션이 어떤 유스케이스를 제공하는지 알 수 없다.


애플리케이션간 구분을 지어보고, 어떤 유스케이스를 제공하는지 알 수 있도록 해보자  
-> AccountService 를 SendMoneySerivce 로 표현을 구체화하기  
-> package-private 접근 제한자로 외부 패키지에서 접근 못하게 하기(해당 접근 제한자는 java의 default 제한자로 아무것도 쓰지 않으면 기본으로 제한함)   
<img width="556" alt="기능으로 구성하기" src="https://github.com/user-attachments/assets/85e6c627-e806-4ef8-9311-ae976cf89f24" />  
<img width="578" alt="Pasted Graphic 18" src="https://github.com/user-attachments/assets/ae87d799-5b02-43ed-90af-75f12d8473be" />

코드만 보고도 어떤 아키텍처인지 알수 있기를 목표로 한 아키텍처임  
<img width="621" alt="image" src="https://github.com/user-attachments/assets/b0e15705-3dc8-44a5-931f-7654f8454f08" />  

<img width="473" alt="image" src="https://github.com/user-attachments/assets/7ef8acb8-75d1-4507-8872-a93325c1be16" />  
