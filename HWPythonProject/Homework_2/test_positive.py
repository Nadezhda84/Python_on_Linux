import subprocess

# tst = "/home/user/tst"
out = "/home/user/out"
# folder1 = "/home/user/folder1"
folder2 = "/home/user/folder2"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    result1 = checkout("cd {}; 7z l arx2.7z".format(out), "qwe")
    result2 = checkout("cd {}; 7z l arx2.7z".format(out), "rty")
    result3 = checkout("cd {}; 7z l arx2.7z".format(out), "add")
    assert result1 and result2 and result3, "test1 FAIL"


def test_step2():
    # test2
    result1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder2), "Everything is Ok")
    result2 = checkout("ls {}".format(folder2), "qwe")
    result3 = checkout("ls {}".format(folder2), "rty")
    result4 = checkout("ls {}".format(folder2), "add")
    assert result1 and result2 and result3 and result4, "test2 FAIL"
