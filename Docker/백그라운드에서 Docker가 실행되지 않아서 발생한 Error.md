## 내용
```
Error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

## 원인
백그라운드에서 Docker가 실행되지 않아서 발생한 Error

## 해결 (Linux)
```
systemctl start docker  # docker 시작
systemctl enable docker # docker 활성화
```
