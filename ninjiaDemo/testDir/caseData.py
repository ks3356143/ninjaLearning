caseData = [
    {
        "id": 1, ##
        'ident': 'TRS_FN_RST_01_001', ##
        'name': "源代码输入功能", ##
        'initialization': "软件正常启动，正常登录进软件", ##
        'premise': '软件正常启动，各界面显示工作正常', ##
        'summarize': '我是测试用例综述', ##
        'designPerson': "李鑫", ##
        'testPerson': '陈小球', ##
        'monitorPerson': '张敏', ##
        "testStep": [
            {
                "operation": '在软件界面中，导入所支持的编程语言如C/C++、C#、Java、PHP、Python、Javascript等可以进行自动化分析和漏洞挖掘',
                'expect': '多种编程语言分析后展示漏洞信息',
                'result': '能够实现多语言检测包含C/C++、C#、Java、PHP、Python、Javascrip，并且能正常查看详细漏洞信息(加图片)',
                'passed': '1',
                'status': "2"
            },
            {
                "operation": '用户输入对应代码仓库的地址、用户名、密码，软件能够从SVN的地址下载相应项目的源代码，并进行分析',
                'expect': '从svn代码仓库完成源代码下载并分析成功',
                'result': 'SVN的地址下载并检测正常(加图片)',
                'passed': '1',
                'status': "2"
            },
            {
                "operation": '用户输入对应代码仓库的地址、用户名、密码，软件能够从Github的地址下载相应项目的源代码，并进行分析',
                'expect': '从github代码仓库完成源代码下载并且分析成功',
                'result': 'Github的地址下载并检测正常(加图片)',
                'passed': '3',
                'status': "1"
            },
        ]
    },
    {
        "id": 2,
        'ident': 'TRS_FN_RST_01_002',
        'name': "支持多种压缩格式",
        'initialization': "软件正常启动，正常登录进软件",
        'premise': '软件正常启动，各界面显示工作正常',
        'summarize': '检查软件支持主流压缩文件格式≥6种，需至少应包括zip、7z、rar、tar、bz、gz等格式',
        'designPerson': "李莉",
        'testPerson': '陈小球',
        'monitorPerson': '张敏',
        "testStep": [
            {
                "operation": '将zip格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': 'Zip压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '能压缩包格式为Zip格式上传后，可以正常检测(加图片)',
                'passed': '1',
                'status': "2"
            },
            {
                "operation": '将7z格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': '7z压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '压缩包格式为7z格式上传后，可以正常检测(加图片)',
                'passed': '1',
                'status': "2"
            },
            {
                "operation": '将rar格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': 'rar压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '压缩包格式为rar格式上传后，可以正常检测(加图片)',
                'passed': '3',
                'status': "2"
            },
            {
                "operation": '将tar格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': 'tar压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '压缩包格式为tar格式上传后，可以正常检测(加图片)',
                'passed': '3',
                'status': "2"
            },
            {
                "operation": '将bz格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': 'bz压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '压缩包格式为bz格式上传后，可以正常检测(加图片)',
                'passed': '1',
                'status': "2"
            },
            {
                "operation": '将gz格式的源代码压缩包上传到软件，检查软件是否识别到源代码语言，并分析出漏洞信息',
                'expect': 'gz压缩包上传成功，软件能够识别出正确的语言信息和漏洞信息',
                'result': '压缩包格式为gz格式上传后，可以正常检测(加图片)',
                'passed': '1',
                'status': "1"
            },
            {
                "operation": '上传损坏的源代码包，检查是否检查到异常',
                'expect': '能够检测到上传的文件错误',
                'result': '能够识别到异常，提升包有误，提示“上传失败：请上传指定格式的源码文件”(加图片)',
                'passed': '1',
                'status': "1"
            },
        ]
    },
]
