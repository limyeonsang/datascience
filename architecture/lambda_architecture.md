## Lambda Architecture
Nathan Marz에 의해 소개된 아키텍쳐로, 실시간 분석을 지원하는 대용량 데이터 처리 아키텍쳐이다.

![](https://bomwo.cc/static/a3e7631959591ea2b1787e0c90c90ff2/0a47e/LambdaArchitrcture.png)
람다 아키텍쳐는 Speed Layer, Batch Layer, Serving Layer로 총 3개의 레이어로 구성되어 있다.

### Speed Layer
실시간 데이터를 처리하고 응답시간을 빠르게 유지하는 역할을 하는 레이어이다. 스트림으로 들어온 데이터를 처리하기 위한 큐나 버퍼같은 구조를 사용하고 효율적인 스트림처리를 위해 증분처리 방식을 사용하고 빠른 데이터 처리, 지연시간을 최소화하는 것을 목표로 한다.   
스피드 레이어의 대표적인 예로는 Apache Spark Streaming,Storm,Flink등이 있다.

### Batch Layer
데이터를 처리하는 단위(분,일,월)로 데이터가 입력되면 해당 설정한 단위로 데이터 처리를 하는 레이어이다. 불변인 데이터들에 대해 배치 작업을 통해 결과 값을 저장한다.   
배치 레이어의 대표적인 예로는 Hadoop, Spark, Hive 등이 있다. 

### Serving Layer
배치레이어와 스피드레이어를 통해 처리된 배치뷰와 실시간뷰를 병합하여 사용자에게 데이터 조회를 제공해주는 레이어이다. 실시간뷰와 배치뷰를 병합해서 보여주는 방법이 일반적이다.    
예로는 Druid, HBase 등이 있다. 

 ### 장단점
 **장점**  
 - 배치, 실시간으로 나뉘어져 있으므로 모든 데이터를 처리하는 기존 방식보다 대용량 처리에 적합한 구조를 갖는다. 
 - 높은 확장성을 가진 구조이다.
 - Near-Real-Time으로 데이터 조회가 가능하다.

 **단점**
 - Batch Layer와 Speed Layer로 분리로 인해 중복 데이터가 존재할 수 있다.
 - 분리된 레이어에 대한 아키텍쳐 관리에 대한 복잡성이 증가할 수 있다.

 ### 카파 아키텍처
 람다 아키텍처의 단점을 보완하기 위해 등장, 데이터 실시간 분석 기능을 수행하기 위해 스피드, 서빙 레이어로 구성된 아키텍처이다.

![](https://bomwo.cc/static/51de195715f9d2417b0814c3e537c355/715a3/kappa-architecture.png)
간단하게 생각하면 람다 아키텍처에서 Batch Layer를 제외한 아키텍처이다.


출처: http://lambda-architecture.net/
http://blog.skby.net/%EB%9E%8C%EB%8B%A4-%EC%B9%B4%ED%8C%8C-%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98/