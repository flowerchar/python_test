import pytest
import yaml

class TestYaml:
    @pytest.mark.parametrize('env', yaml.safe_load(open('data.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print('这是测试环境')
            print(f"测试环境的ip是：{env['test']}")
        elif 'dev' in env:
            print('这是开发环境')
            print(f"开发环境的ip是：{env['dev']}")
        elif 'pro' in env:
            print('这是生产环境')
            print(f"生产环境的ip是：{env['pro']}")
        else:
            print('环境信息错误')