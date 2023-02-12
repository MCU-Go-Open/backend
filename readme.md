# MCU Gopen 後端(FastAPI)

打包 docker image
```
docker build -t mcu_gopen_backend . --no-cache
```
執行環境
```
docker run -d -p 8080:8080 --name mcu_gopen_backend  mcu_gopen_backend
```