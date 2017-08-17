file_path=${0%/*}
work_dir="$file_path/../"
cd $work_dir
test -d venv || virtualenv venv
source venv/bin/activate
pip install -r requirements
deactivate
./venv/bin/supervisord -c etc/supervisord.conf

