# FileSizeDigitAnalyzer


如果出现库不存在的情况，请安装对应的库：
```
pip install pandas
pip install matplotlib
```
## 背景介绍
灵感来自于毕导的视频[【毕导】这个定律，预言了你的人生进度条](https://www.bilibili.com/video/BV1VrVSz1Eme)。

该视频的主要内容为：本福特定律揭示了自然界中许多现象的对数分布特征，通过数学证明和对数坐标的展示，解释了为什么自然界的数据会呈现出对数均匀分布的特性。同时，视频还探讨了这种分布对人类感知的影响，指出人类大脑在对数尺度上感知世界使得我们能够在不同尺度上体验世界的多样性。此外，视频还强调了对数系统的重要性，如果我们没有对数系统，而是线性感知的生物，那么我们将只能二选一。津巴多在普通心理学中写道，知觉赋子感觉以意义，而不是对世界的完美表征。因此，我们对世界的认识是对世界的解释，而不是对世界的完美表征。我们恰好遇到宇宙对数的分布，冰冷的数字在这里有了温度，物体和心灵达成完美的交互。（由bilibili AI小助手总结）

在评论区中我看到了有人使用电脑文件的大小验证视频内容，可惜没有给出源码与实验结果。此外，视频的不少观众认为常用的十进制导致1的出现最多，换别的进制结果就不一定一样了。于是我添加了查看不同进制下分布情况的功能。
为了验证视频内容和评论区中的各种猜想，我使用python编写能实现该功能的程序。

## 程序介绍
该程序的功能为：windows用户输入盘符，程序统计该盘符所有文件的大小的首位字符和第二位字符的数量分布，并使用直方图呈现。用户还可以选择文件大小的进制（2-16），研究进制对结果的影响。

## **我的实验结果**
使用D盘（989083个文件）、F盘（34800个文件）、E盘（148628个文件）分别进行测试，首位数字的分布整体呈现对数分布，有部分峰值，但1确实是出现最多的；第二位数字整体呈现均匀分布；进制的选择并不影响结果。以下仅呈现D盘的实验结果。
![2](https://github.com/user-attachments/assets/326d1029-082d-4d8d-bd43-d05a55504afe)
![16](https://github.com/user-attachments/assets/10a3b83e-c3d2-4d01-9822-d9a0087c297e)
![15](https://github.com/user-attachments/assets/99bd335f-bbaa-42f9-bd6f-130f6304e89d)
![14](https://github.com/user-attachments/assets/aedac734-56ab-4b9b-b04b-59dee6e54b36)
![13](https://github.com/user-attachments/assets/fff0ffce-7be4-49d7-96ad-ad16f3d37c50)
![12](https://github.com/user-attachments/assets/8a53bff8-e5e8-4309-b5d0-53096b748e5e)
![11](https://github.com/user-attachments/assets/37b9f682-a2cd-4152-83cb-24ff80013874)
![10](https://github.com/user-attachments/assets/ba6e839c-953a-461c-ad10-0e8401dde4d9)
![9](https://github.com/user-attachments/assets/07bbbab4-669c-4c5b-b679-9097bb16be2f)
![8](https://github.com/user-attachments/assets/cb8c0121-48b2-49bb-83cd-e9ed3ce37980)
![7](https://github.com/user-attachments/assets/b25775fb-4145-4a6a-9632-051cfd53e1db)
![6](https://github.com/user-attachments/assets/b07f8b50-4c5e-4548-9f42-0cc61b30de3b)
![5](https://github.com/user-attachments/assets/c6942907-df7d-48af-a15b-9e0a830d0c73)
![4](https://github.com/user-attachments/assets/2a384d44-4838-4c03-a0ed-ed88a4dc4131)
![3](https://github.com/user-attachments/assets/c1179d07-848b-45c2-ac39-67636d4477c3)

希望这个程序可以帮助你通过自己电脑就可以直观地感受到视频中的内容。

感谢TRAE、 deepseek的深入参与。❤❤❤
