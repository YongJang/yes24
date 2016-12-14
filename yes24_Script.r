# 작업 디렉토리 설정
setwd("D://R/")
# 크롤링 한 csv 파일 읽기
yes24 <- read.csv("yes24.csv")

# 상위 몇 줄만 출력
head(yes24)
# 전체 출
yes24

# 데이터 형태 보기
str(yes24)

# 결측치 제거
yes24_na <- na.omit(yes24)
yes24_na <- data.frame(yes24_na, stringsAsFactors = F)

str(yes24_na)

#Factor를 num으로 변경 (에러 해결해서 안쓰임)
#yes24_na$PageNum <- as.numeric(as.character(yes24_na$PageNum))
#yes24_na$PageNum <- suppressWarnings(as.numeric(as.character(yes24_na$PageNum)))

yes24_na
# 기초 통계량 요약
summary(yes24_na)

# 산점도(scatter plot)
plot(yes24_na$PageNum, yes24_na$Price, xlab="Page Number", ylab="Price", pch="+")
plot(yes24_na$Weight, yes24_na$Price, xlab="Weight", ylab="Price", pch="+")
plot(yes24_na$Volume, yes24_na$Price, xlab="Volume", ylab="Price", pch="+")

#jitter
plot(jitter(yes24_na$PageNum), jitter(yes24_na$Price), xlab="Page Number", ylab="Price", cex=.2)


# 가격과 페이지 수에 대한 피어슨 상관 계수
cor(yes24_na$Price, yes24_na$PageNum)
# 가격과 무게
cor(yes24_na$Price, yes24_na$Weight)
# 가격과 부피
cor(yes24_na$Price, yes24_na$Volume)

# 통계적 유의성 검증
cor.test(yes24_na$Price, yes24_na$PageNum, method = "pearson")
cor.test(yes24_na$Price, yes24_na$Weight, method = "pearson")
cor.test(yes24_na$Price, yes24_na$Volume, method = "pearson")

# 단순선형회귀 분석
# 가격 - 페이지 수
m <- lm(yes24_na$Price ~ yes24_na$PageNum, yes24_na)
m
summary(m)
plot(yes24_na$PageNum, yes24_na$Price, xlab="Page Number", ylab="Price", pch="+")
abline(coef(m))
# 가격 - 무게
m <- lm(yes24_na$Price ~ yes24_na$Weight, yes24_na)
m
summary(m)
plot(yes24_na$Weight, yes24_na$Price, xlab="Weight", ylab="Price", pch="+")
abline(coef(m))
# 가격 - 부피
m <- lm(yes24_na$Price ~ yes24_na$Volume, yes24_na)
m
summary(m)
plot(yes24_na$Volume, yes24_na$Price, xlab="Volume", ylab="Price", pch="+")
abline(coef(m))

# 중선형회귀 분석
m <- lm(yes24_na$Price ~ yes24_na$PageNum + yes24_na$Weight + yes24_na$Volume, data = yes24_na)
m
coef(m)
summary(m)

# 책 가격과 책의 밀도 간의 상관 관계
c <- yes24_na$Weight/yes24_na$Volume
cor(yes24_na$Price, c)
