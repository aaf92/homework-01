import subprocess

def run_job(cmd):
    ret = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return ret.stdout.decode(('UTF-8'))
    
if __name__ == '__main__':
    # Run
    output = run_job("./assign1.sh hello")
    assert output == "hello"
