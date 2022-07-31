# 项目执行者：余晨阳（项目由个人完成）
# 已完成部分
1.SM3实现与优化
2.SM3的生日攻击
3.SM3的rho攻击
4.SM3的长度扩展攻击
5.SHA256的实现
6.Merkel树的实现
# sha256
本质上是一种哈希函数，把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值（哈希值）的指纹。
![sha256 1111111](https://user-images.githubusercontent.com/109857507/182001848-d86c73b1-c4eb-492d-b241-e3de1ff22c80.png)
# MerkelTree
（1）对data blocks分别计算哈希值（采用sha256算法）； （2）每层两两计算获得哈希值，并将每一层的hash值从左到右存放在一个列表中。 （3）直至计算至最上一层，得到根节点。
![111](https://user-images.githubusercontent.com/109857507/182002115-6b5df4db-028f-4d67-94df-e6c14d0a5a3f.png)
