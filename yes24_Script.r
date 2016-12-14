# �۾� ���丮 ����
setwd("D://R/")
# ũ�Ѹ� �� csv ���� �б�
yes24 <- read.csv("yes24.csv")

# ���� �� �ٸ� ���
head(yes24)
# ��ü ��
yes24

# ������ ���� ����
str(yes24)

# ����ġ ����
yes24_na <- na.omit(yes24)
yes24_na <- data.frame(yes24_na, stringsAsFactors = F)

str(yes24_na)

#Factor�� num���� ���� (���� �ذ��ؼ� �Ⱦ���)
#yes24_na$PageNum <- as.numeric(as.character(yes24_na$PageNum))
#yes24_na$PageNum <- suppressWarnings(as.numeric(as.character(yes24_na$PageNum)))

yes24_na
# ���� ��跮 ���
summary(yes24_na)

# ������(scatter plot)
plot(yes24_na$PageNum, yes24_na$Price, xlab="Page Number", ylab="Price", pch="+")
plot(yes24_na$Weight, yes24_na$Price, xlab="Weight", ylab="Price", pch="+")
plot(yes24_na$Volume, yes24_na$Price, xlab="Volume", ylab="Price", pch="+")

#jitter
plot(jitter(yes24_na$PageNum), jitter(yes24_na$Price), xlab="Page Number", ylab="Price", cex=.2)


# ���ݰ� ������ ���� ���� �Ǿ ��� ���
cor(yes24_na$Price, yes24_na$PageNum)
# ���ݰ� ����
cor(yes24_na$Price, yes24_na$Weight)
# ���ݰ� ����
cor(yes24_na$Price, yes24_na$Volume)

# ����� ���Ǽ� ����
cor.test(yes24_na$Price, yes24_na$PageNum, method = "pearson")
cor.test(yes24_na$Price, yes24_na$Weight, method = "pearson")
cor.test(yes24_na$Price, yes24_na$Volume, method = "pearson")

# �ܼ�����ȸ�� �м�
# ���� - ������ ��
m <- lm(yes24_na$Price ~ yes24_na$PageNum, yes24_na)
m
summary(m)
plot(yes24_na$PageNum, yes24_na$Price, xlab="Page Number", ylab="Price", pch="+")
abline(coef(m))
# ���� - ����
m <- lm(yes24_na$Price ~ yes24_na$Weight, yes24_na)
m
summary(m)
plot(yes24_na$Weight, yes24_na$Price, xlab="Weight", ylab="Price", pch="+")
abline(coef(m))
# ���� - ����
m <- lm(yes24_na$Price ~ yes24_na$Volume, yes24_na)
m
summary(m)
plot(yes24_na$Volume, yes24_na$Price, xlab="Volume", ylab="Price", pch="+")
abline(coef(m))

# �߼���ȸ�� �м�
m <- lm(yes24_na$Price ~ yes24_na$PageNum + yes24_na$Weight + yes24_na$Volume, data = yes24_na)
m
coef(m)
summary(m)

# å ���ݰ� å�� �е� ���� ��� ����
c <- yes24_na$Weight/yes24_na$Volume
cor(yes24_na$Price, c)
