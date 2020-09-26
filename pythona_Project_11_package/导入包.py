import python_package_1

# 只有在__init__中定义了才能调用
python_package_1.send_message.send("hahaha")
txt = python_package_1.receive_message.receive()
print(txt)