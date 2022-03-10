isPythonExist="which python3"

if eval $isPythonExist; then
	echo "Python3 is already installed... Skipping python3 installation"
else  
	sudo apt-get update
	sudo apt-get isntall python3 -y
fi

python3 -m venv $(pwd)/venv

. $(pwd)/venv/bin/activate

requirements="$(pwd)/requirements.txt"


pip install -r $requirements
 
message="\n\n설치 완료\n'bash runDjangoServer.sh' 명령어를 이용하여 장고 서버를 실행합니다. 장고 서버의 포트 번호는 8000 입니다.\n가상 환경을 종료하시려면 'deactivate'를 입력하십시오.\n"

printf $message
