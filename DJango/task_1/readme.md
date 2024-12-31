1. kubectl create namespace argocd :  create name space 
2. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml : apply content from this repo

3. install argocd
4. kubectl patch svc argocd-server -n argocd -p '{"spec": "LoadBalancer"}}' : to change from clusterIP to LoadBalancer

5. kubeclt port-forward svc/argocd-server -n argocd 8080:443 : port  forward
6. kubectl -n argocd get secret argocd-initia-admin-secret -o jsonpath="{.data.password}" | base64 -d echo : for get initial generated passwrod
