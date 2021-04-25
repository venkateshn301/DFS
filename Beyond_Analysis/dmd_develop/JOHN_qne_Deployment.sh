# How to run 

# https://bitbucket.org/beyondanalysis/qne/src/dod_develop/
#git clone https://Beyond_John@bitbucket.org/beyondanalysis/qne.git 
sudo apt-get install chromium-browser
repo="$PWD"

echo " Deployment Started "
echo " New folder created in ="$PWD"  = /home/$username/Documents   "
#################
echo  "$repo/qne\ docker/"
#####
cd $repo/qne\ docker/
echo  "$PWD"   


docker build . -t  ubuntu:14.04_basic

cd $repo/qne\ docker/qne_subcontainer
echo "$PWD"
docker build . -t qne:tp

docker run -dit -v $repo:/home/Sandbox/qne -p 5432:5432 -p 80:80 -p 443:443 -p 8080:8080 -p 60:60 -p 3000:3000 -p 6379:6379 --name beyond-analysis-tp qne:tp


docker ps -a

docker exec -it  beyond-analysis-tp  bash 

echo  "Now you are in the Docker  container"
echo "service redis-server start" 
echo  " service postgresql start" 

echo "cd /home/Sandbox/qne"
echo  "apt-get install build-essential "
echo  "cd  /home/Sandbox/qne/mediator  "
echo  "npm rebuild zmq  " 
echo  "npm install -g gulp-cli  "
echo  "npm install -g cake  "
echo  "cd  /home/Sandbox/qne/shared "
echo  "cake install " 
echo " cd  /home/Sandbox/qne/nginx "

echo  "npm run build  " 
echo "npm start " 
echo "end  " 


