# Boostcamp AI Tech 3기: NLP-05-외않되조

---

# Project: 문장 내 개체간 관계 추출

- Wrap-up Report : [프로젝트_Wrap_Up.pdf](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-05/files/8549846/_Wrap_Up.pdf)
- 발표자료 : [베이징 동계 올림픽 데이터 제작 소개.pdf](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-05/files/8549847/default.pdf)

## Members

| 이름      | Github Profile | 역할 |
| ---       | --- | --- |
| 공통      |     | 가이드라인 작성, Entity•Relation 정의, 파일럿 및 메인 어노테이션 |
| 강나경    | [angieKang](https://github.com/angieKang) | 카테고리별 문장 split, fleiss-kappa 계산 |
| 김산      | [mounKim](https://github.com/mounKim) | 가이드라인 FAQ 작성 |
| 김현지    | [TB2715](https://github.com/TB2715) | 데이터셋 전처리, 가이드라인 이미지 제작  |
| 정민지    | [minji2744](https://github.com/minji2744) | 모델 Fine-tuning, 데이터셋 분석 |
| 최지연    | [jeeyeon51](https://github.com/jeeyeon51) | 여러 개의 파일을 카테고리별로 분류하여 통합 |

## 문제 개요

본 프로젝트에서는 **2022 베이징 동계 올림픽**과 관련된 위키 원시 말뭉치를 활용해 자연어처리 **관계 추출 태스크**에 쓰이는 주석 코퍼스를 제작했습니다. 프로젝트의 의의는 한국어 및 다른 언어에서의 자연어처리 데이터셋의 유형 및 포맷이 어떠한지, 그리고 데이터셋을 구축하는 일반적인 프로세스가 무엇인지 학습하는 것입니다.

## 프로젝트 수행 절차 및 방법

![Untitled](https://user-images.githubusercontent.com/59854630/164980684-c9111310-34f2-431b-b027-238033d2d7cb.png)


## 데이터셋 소개

- 베이징 동계 올림픽 관련 위키 데이터
- 총 43개의 문서, 문장 1,693개로 구성
- 예시
    > 🏅 2022년 동계 올림픽은 2022년 2월 4일부터 2월 20일까지 중화인민공화국 베이징에서 열린동계 올림픽이다.
    

### 정의된 Relations
- 총 9개의 entity, 13개의 relation 정의
- 가이드라인 : [guideline.pdf](https://github.com/boostcampaitech3/level2-data-annotation_nlp-level2-nlp-05/files/8549876/05_guideline.pdf)

![Untitled 4](https://user-images.githubusercontent.com/59854630/164980916-d76f7b4b-865a-41f7-84bf-d73d8da7d406.png)





## 실험 결과

### 작업자간 일치도
- fleiss-kappa : 0.937

### 모델 Fine tuning

```
    train(0.6), validation(0.2), test(0.2)
    klue/roberta-large, epochs: 20, learning rate: 2e-5, batch size: 32
```

-  validation micro f1 score : 59
-  test set evalution micro f1 score : 55

![output](https://user-images.githubusercontent.com/59854630/164981173-401258ba-554a-41ad-a5e1-32721f7ace60.png)
