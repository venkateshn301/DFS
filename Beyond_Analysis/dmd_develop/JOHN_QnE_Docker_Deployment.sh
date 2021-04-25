# How to run 

# https://bitbucket.org/beyondanalysis/qne/src/dod_develop/
#git clone https://Beyond_John@bitbucket.org/beyondanalysis/qne.git 

repo="$PWD"

echo " Deployment Started "
cd /home/Sandbox/qne
echo  "$PWD"   


echo  "Now you are in the Docker  container"
service redis-server start 
service postgresql start

cd /home/Sandbox/qne
echo "$PWD  ++++++++++++++++++++++++++++++"
apt-get install build-essential 
cd  /home/Sandbox/qne/mediator
echo "$PWD"
echo "NPM  Next ++++++++++++++++++++++++++++ " 
npm rebuild zmq 
npm install -g gulp-cli  
npm install -g cake  
cd  /home/Sandbox/qne/shared
echo "$PWD  ++++++++++++++++++++++++++++++++"
echo "CAKE install next" 
cake install 
 cd  /home/Sandbox/qne/nginx 
echo "$PWD  +++++++++++++++++++++++++++++++++"
npm run build 
npm start 
echo "end  " 


