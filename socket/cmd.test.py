import subprocess

a = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)
print(a)
print(a.stdout.read())