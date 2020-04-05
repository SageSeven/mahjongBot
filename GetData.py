import json


def get_data():
    input_str = input()
    try:
        full_input = json.loads(input_str)
    except Exception as err:
        print(err)
        print("ppppppppp")
        print(input_str)
        print("qqqqqqqqq")
        return "1 0 0"

    if "data" in full_input:
        my_data = full_input["data"]  # 该对局中，上回合该Bot运行时存储的信息
    else:
        my_data = None

    # 分析自己收到的输入和自己过往的输出，并恢复状态
    all_requests = full_input["requests"]

    all_responses = None
    if "responses" in full_input:
        all_responses = full_input["responses"]

        for i in range(len(all_responses)):
            my_input = all_requests[i]  # i回合我的输入
            my_output = all_responses[i]  # i回合我的输出
            # TODO: 根据规则，处理这些输入输出，从而逐渐恢复状态到当前回合
            pass

    # 看看自己最新一回合输入
    curr_input = all_requests[-1]
    return curr_input
