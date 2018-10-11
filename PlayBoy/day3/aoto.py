# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

def generateDynamicScript(
        script_content: str,
        script_type: str,
        param: str = "",
        extra_param: str = "",
        extend_dict: dict = None):
    """
    动态生成脚本文件
    :param script_content: 脚本内容
    :param script_type: 脚本类型，用于拼接文件名的后缀
    :param param: yaml格式的参数，用于替换动态参数
    :param extra_param: 扩展参数，yaml格式的参数，用于替换动态参数
    :param extend_dict:字典类型的扩展参数，用于替换动态参数
    :return: 脚本文件的名称，脚本的完整路径
    """
    logger.info("动态生成脚本文件")

    script_content = script_content.replace('\r', '')

    logger.info("填写动态变量")

    # 动态参数用${key}这样的结构存放,提取出所有的动态参数
    params = re.findall('\${(.*)}', script_content)
    if param != "" and params != "":
        yaml_params = yaml.load(param)
        for cmd_param in params:
            if ':' in cmd_param:
                script_content = script_content.replace('${%s}' % cmd_param,
                                                        yaml_params.get(cmd_param.split(":")[1]))

    if extra_param is not None and extra_param != "":
        yaml_params = yaml.load(extra_param)
        for cmd_param in yaml_params:
            script_content = script_content.replace('${%s}' % cmd_param, yaml_params.get(cmd_param))

    if extend_dict is not None:
        for k in extend_dict:
            script_content = script_content.replace('${%s}' % k, extend_dict[k])

    uid = uuid1().__str__()
    scriptPath = PACKAGE_PATH + uid + '.' + script_type
    output = open(scriptPath, 'wb')
    output.write(bytes(script_content, encoding='utf8'))
    output.close()
    logger.info("写入文件结束，文件为%s", scriptPath)
    return uid, scriptPath
