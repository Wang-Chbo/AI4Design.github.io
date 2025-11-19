# 使用豆包api

关于api的原理：

【如何理解API，API 是如何工作的 - CSDN App】https://blog.csdn.net/cumtdeyurenjie/article/details/80211896?sharetype=blog&shareId=80211896&sharerefer=APP&sharesource=qq_62814785&sharefrom=link

查看文本生成部分的文档说明

链接：https://www.volcengine.com/docs/82379/1399009

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=MjEwNDY0NWMyMjhlZjczNTNiNzEwZDlhOGFkZWIwZjRfZU9LYzFJMDRYaXBFT1N0am1YUWEzWWhacm5pZVNDVTRfVG9rZW46VG42VWJyTTVkb1FaSld4b2E3VmM0U2hQbkhmXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

完成前提条件中的内容然后使用python进行示例代码的运行就可以进行api的调用从而实现文本生成
点击获取api跳转

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=NDA0MDc5ODViOWU2NzJiMjQ1OWZhOWQyZTk3MTM2YzlfZFkwdVNJeXNqcDE2T3VoODZVTWtWYUJka1dMRHZkNTdfVG9rZW46WlkzSGJZS1pCbzlhUG14R2hydmNGcVBMbmVjXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

直接创建即可

# 配置一下api

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=NmE5YTNjYjFlZWIwZDY3MzMxYjczYTgxYTFiOGNmY2RfQWR5RnM3VGgybHd2dmpoUEhQUTgzaENCY0w0UlZEWkNfVG9rZW46RXdxeWI3VmlEb3ViZnR4Q2ozWmNTMkdLbmdoXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=YTUyMDJkNTMzZjZiZDZjMGNlYjhkZWI4NDYxNjM0ZDBfREt4VEU3bjFnVTFkb0hwZDFtTExFQXEzSWxGQ0k3OUZfVG9rZW46VGRZemJueWNOb2QzTVp4eXB3cmNBSFl5bnphXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

```Bash
#配置apikey到环境变量中（临时）
export ARK_API_KEY="<ARK_API_KEY>"
#永久
echo 'export ARK_API_KEY="你的实际密钥"' >> ~/.zshrc
```

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=MzllZDRkZjk1OTRiMzYzYzNhNjUxYzRiMWE5ZTllMzJfZTdDeVZxWW9qclBlV2FZekJ0ckNxdFNVMExpUWhmQVBfVG9rZW46TkFjOGJDcWNwb2k5Vm54RGd5NmNVT1lJbnJkXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

# Access key鉴权

关于这里的access key鉴权，先获取access key

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=NWFjMDU1MWZjNzE3NjAxMGU2NmYwN2Q2NTI1OGMzMWJfYWlZVklJeWdjRjdFRFhYeFlHdWNsRVFyZXNnOWdaWVJfVG9rZW46WklQeWJhNHdxb1k0bmd4Q3AzUmMyeDhjbkNiXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

直接新建应该就可以了

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=OTMyMjM0NTU1NmYwMmY0YmM4YmI3MThmYzAxOGI2M2JfUnVsQmlIODNWbzRNSVFTeGxwVXNNMFoxR0haNVBGdzZfVG9rZW46SktRVmIxMTZyb1NlWVB4UWxUb2MwUllDbm5iXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

# 接入测试

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=NDk5MjIzY2M5YWQ0NDFhMzZmMGJhZTg0MjJlYWE1NzlfZ1JnZlZEOURtaUNSU2xubEJLNFN2QlhUTzI5MnpOTDZfVG9rZW46QWxMUWJCbzQ1bzJhTFJ4SElCVGNuNUIyblRoXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

使用火山引擎的sdk进行测试

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=YjRiZjk0OWIxNzlmZmQzYzFjNzA3MGZkMzI4NzJhMDZfZE92Z0M4MXhvUDZ0Y2FaWEJDU2EyYzRaYURZQXNOc0tfVG9rZW46Tmw0MWJVSkRTb2Fma1l4MW5meGM3YnZIbm9kXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

# endpoint

获取endpoint：https://www.volcengine.com/docs/82379/1099522

![](https://kcnvj21glvf4.feishu.cn/space/api/box/stream/download/asynccode/?code=NjM3MDc1NzhhOWJkNGE4MjVmOGJjYmJkODllM2MxZDdfYjBoV1I3dllhUHQyeTRRbzJzalZTWWxBOXBZZmtPakxfVG9rZW46QVlSamJaRzBVb00wdU54amN4TmNZVTBCbk9nXzE3NjM1NjQwMDI6MTc2MzU2NzYwMl9WNA)

直接进行创建即可

这里需要和我们的模型id以及api key进行绑定，相当于另一种调用api的方式

## Summary

总结一下，我们这里主要使用python进行api的调用，调用过程就是将指定格式作为输入获取大模型的输出，并以指定格式进行返回。

主要获取的是：api_key（刚需）

ak(access key) sk(secret key)

model_name:模型名字

endpoint：在线推理接入点
