#### 自然语言处理任务

- 文本理解
  - 实体消歧
  - 指代消解
- 信息抽取
  - 命名实体识别
  - 关系抽取
  - 模版填充
- 文本生成
  - 机器翻译
  - 对话任务
  - 自动摘要
- 文本分类
  - 情感分析
- 信息检索

#### RNN

提出的原因：

为了解决普通前馈神经网络以及卷积神经网络在处理不定长句子中，无法准确预估参数以及无法对句子整体语义进行感知的问题。

如何解决：

首先，采用与卷积神经网络类似的权重共享思想，对每个Cell，采用同一个权重张量W。其次，使用记忆单元h，在每个时间步中，计算上一步的h以及刷新h。

结构图如下：

![](https://miro.medium.com/max/1400/1*WMnFSJHzOloFlJHU6fVN-g.gif)
$$
  h_t = \sigma(W_{xh}x_t + W_{hh}h_{t-1}+b) \\
  o_t = g_\phi(h_t)
$$
$$a = 2$$
其中，sigma函数为激活函数。以上便是基础的循环神经网络。

#### LSTM

提出的原因：

由于RNN结构，当输入🍊过长时，由于权重张量的累乘，当`Whh<1`时，会出现梯度弥散，当`Whh>1`时，会出现梯度爆炸。  

$$ \frac{\partial h_t}{\partial h_i} = \prod_{j=i}^{t-1}diag(\sigma'(W_{xh}x_{j+1}+W_{hh}h_j+b))W_{hh}$$
因此，在处理长句时，RNN存在短时记忆与训练困难的问题。

如何解决？：

LSTM在RNN的基础上，新增了一个状态向量C，同时引入了门控机制，通过输入门、遗忘门、输出门来控制信息的遗忘和刷新。结构如图所示：

![](https://miro.medium.com/max/1400/1*0f8r3Vd-i4ueYND1CUrhMA.png)

与RNN结构不同，LSTM将输出向量与记忆单元分为两个变量，分别是c与h。

**遗忘门**用于控制上一步的状态变量`c_{t-1}`，计算公式为：
$$
g_{f} = \sigma(W_f[h_{t-1},x_t] + b_f)
$$
激活函数常采用sigmoid，当gf接近0时，表示遗忘前面的隐藏层状态，否则为keep

**输入门**用于控制对输入接受的程度：
$$
c' = tanh(W_c[h_{t-1},x_t] + b_c) \\
g_i = \sigma(W_i[h_{t-1},x_t] + b_i)
$$
其中，gi为门控变量，控制对c'的接受程度，激活函数常采用sigmoid。

经过输入门与遗忘门之后，对状态变量C进行更新：
$$
c_{t} = g_fc_{t-1} + g_ic'
$$
**输出门**用于有选择地输出变量，门控变量`g_o`为：
$$
g_{o} = \sigma(W_o[h_{t-1},x_t] + b_o)\\
h_{t} = g_o tanh(c_t)
$$
其中，门控变量的计算通常采用sigmoid函数，因此控制在[0,1]之间。

| 输入门控 | 遗忘门控 | LSTM行为       |
| -------- | -------- | -------------- |
| 0        | 1        | 只使用记忆     |
| 1        | 1        | 综合输入和记忆 |
| 1        | 0        | 输入覆盖记忆   |
| 0        | 0        | 清零记忆       |

关于LSTM是如何在结构上解决梯度消失和梯度爆炸的，贴一个[链接](https://www.zhihu.com/question/44895610)

#### GRU

提出的原因：

LSTM结构相对比较复杂，计算代价较高，参数量较大。

如何解决：

通过对LSTM结构进行简化，将状态变量和输出向量合并，统一为状态向量h，同时，减少门控数量为2个：复位门和更新门。

![](https://miro.medium.com/max/1400/1*jhi5uOm9PvZfmxvfaCektw.png)

复位门：用于决定遗忘多少的前面的隐层状态信息。
$$
g_r = \sigma(W_r[h_{t-1},x_t]+b_r) \\
h' =  tanh(W_o[g_rh_{t-1},x_t] + b_o)
$$
更新门：类似于LSTM的输入门和遗忘门，用于决定信息的接纳与丢弃。
$$
g_u = \sigma(W_u[h_{t-1},x_t]+b_u) \\
$$
输出为：
$$
h_{t} = (1-g_u)h_{t-1} + g_uh'
$$
GRU相比于LSTM，具有更精简的结构，训练速度更快，但在效果上并不一定好于LSTM，一般需要对两者进行比较。

#### BiLSTM

双向LSTM，即对输入序列，采用正向、反向进行计算并拼接结果。可以更好地捕捉双向的语义依赖。这种结构不仅限于LSTM，在RNN、GRU都可以使用双向，提高模型效果。

#### word Embedding

词嵌入，将词语映射为一个向量表示。

word2vec模型是一种经典的Embedding方法。

#### Transformer

#### Attention

#### Bert

#### Encoder-Decoder/Seq2Seq

#### 参考内容

[Illustrated Guide to LSTM’s and GRU’s: A step by step explanation](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)

