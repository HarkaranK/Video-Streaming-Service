# Video-Streaming-Service

Harkaran -WSL

For rebuilding if changes to image aren't taking place
- docker-compose up -d --build

To build images
- docker build -t authentication ./authentication
- docker build -t filesystem ./filesystem
- docker build -t mysql ./mysql
- docker build -t upload ./upload
- docker build -t video_stream ./video_stream


Kubernetes
```
kubectl apply -f .\kubernetes-configs\uploaded-videos-pv.yaml
kubectl apply -f .\kubernetes-configs\uploaded-videos-pvc.yaml
kubectl apply -f .\kubernetes-configs\mysql-pvc.yaml
```

```
kubectl apply -f ./authentication/video-streaming-service-authentication.yaml
kubectl apply -f ./filesystem/video-streaming-service-filesystem.yaml
kubectl apply -f ./mysql/video-streaming-service-mysql.yaml
kubectl apply -f ./upload/video-streaming-service-upload.yaml
kubectl apply -f ./video_stream/video-streaming-service-video_stream.yaml
kubectl apply -f .\kubernetes-configs\loadbalancer.yaml
```

```
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get pvc
```

```
kubectl delete deployments --all
kubectl delete services --all
kubectl delete pods --all
kubectl delete pvc --all
kubectl delete pv --all
```
