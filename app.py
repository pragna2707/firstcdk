from aws_cdk import core
from my_stack import MyStack


app = core.App()
MyStack(app, 'MyStack')
app.synth()