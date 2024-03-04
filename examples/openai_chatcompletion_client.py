# _*_ coding: utf-8 _*_
import time

from openai import OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://10.10.106.240:8008/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id
print("model_id:", model)
stream = False
while True:
    prefix = time.time() * 1000
    '''
    chat_completion = client.chat.completions.create(
        messages=[{
                "role": "system",
                "content": "You are an assistant entity for the Customs Import and Export Tariff of the People's Republic of China. Output HSCODE based on user input"
            }, {
            "role": "user",
            "content": "请介绍一下你自己"
            },
            {
                "role": "assistant",
                "content": "您好，我是壹沓科技研发的供应链LLM大模型，我的姓名是CubeLLM。"
            }, {
                "role": "user",
                "content": "和我讲一个绕口令"
            }],
        stop=["<|endoftext|>", "<|im_end|>"],
        model=model,
        stream=stream
    )
    '''


    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": "请介绍一下你自己"
        },
        {
            "role": "assistant",
            "content": "您好，我是壹沓科技研发的供应链大模型，我的名字是CubeLLM，是一个14B参数量的模型，本身具备大模型的基础能力，欢迎与我沟通交流。"
        },
        {
            "role": "user",
            "content": "供应链是什么，请介绍一下"
        }],
        stop=["<|endoftext|>", "<|im_end|>"],
        model=model,
        stream=stream
    )

    '''
    chat_completion3 = client.chat.completions.create(
        messages=[{
            "role": "system",
            #"content": "You are a helpful assistant."
            "content": "角色：希望你扮演一个九阳公司的情感语义判断助手，九阳公司主要从事小家电、家具清洁小家电系列产品的生产销售。九阳品牌主要涵盖豆浆机、破壁机、电饭煲、洗碗机等。要求：1、返回文章的情感语义，分3类：中立、正面、负面；2、返回文章的10个关键词、10个正面词、10个负面词；3、输出严格按照：情感语义、关键词、正面词、负面词返回结果，不要有任何的扩展；4、不相关问题一律拒绝回答"
        }, {
            "role": "user",
            "content2": "使用python,写一个贪吃蛇的程序",
            "content1": "千年舟椰奶白奥松板的柜门，千年舟多层板柔光暖白橱柜，鲁丽欧松板的柜体，希望没翻车。大家组装柜子都是啥色啊@佑佑不哭 #环保板材 #衣柜橱柜OCR:|也不知道他妈的谁发明的装修|为什么要装修|DTC 他不像吗|DTC 我就说装修哪有他妈不疯的|你以为硬装完了就可以熬到头了|软装更他妈费钱|顶框框框框顶几个月|所有的身价都花进去了|还他妈的不出效果|高端全属定 剧全",
            "content": "2023年12月20日-22日，以“聚势、突破、跨越”为主题的“2023年优材联盟越州嘉年华大会”在江南名城绍兴举行。嘉年华大会内容丰富，更有部品品牌代表在家装渠道的分享交流。 用优秀的产品和服务，携手装企完成作品，做品质家装的坚定支持者和守护者，是恒洁卫浴既定的家装渠道策略，也是恒洁近年来在家装渠道获得重大突破的第一性原理。 恒洁卫浴家装事业部总经理谢永成以《选品质就是选生活》为题，分享家装渠道发展经验，获得好评，更戳中与会企业家装渠道负责人的痛点、产生强烈共鸣。他从“战略重视、组织先行、合作定位、产品驱动、干法赋能、渠道全开、服务保障",
            "content3": "近来天气阳光明媚，只是早晚温差较大！大家都要注意保暖💖今天要感谢曾美俩夫妻对千年舟品牌的认可，我们说的千好万好，还不如客户一句的口碑好#年底还需要订制衣柜的朋友赶紧不单，时间不等人🤝👏"
        }],
        stop=["<|endoftext|>", "<|im_end|>"],
        model=model,
        stream=stream
    )
    '''


    if not stream:
        print("Chat completion results:")
        print(chat_completion)
        print(chat_completion.choices[0].message.content)
    else:
        result_text = ''
        for info in chat_completion:
            content = info.choices[0].delta.content
            if content is None:
                continue

            result_text = result_text + content

        print(result_text)

    postfix = time.time() * 1000
    total_time = postfix - prefix
    print("total_time:", total_time)
