from subprocess import run as subprocessrun

command = "sqlite3; .open tf.db; .tables";

ret = subprocessrun(command, capture_output=True, shell=True)

out = ret.stdout.decode()

print(out)
