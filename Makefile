AWS_REGION ?= us-east-2
SERVICE_NAME ?= api
AWS_ACCOUNT_ID ?= 774218618828
EKS_CLUSTER_NAME ?= prod-1
LAMBDA_FUNCTION_NAME ?= IdoWebsite
AWS_PROFILE ?= default

setup:
	touch .env

run-local:
	docker compose -f 'docker-compose.yml' up -d --build

build-frontend:
	(cd frontend; npm ci; npm run build)
	rm -rf ./app/public
	mv ./frontend/build ./app/public

build-lambda:
	(zip -r aws_lambda_artifact.zip ./app)


deploy-all: 
	make build-frontend
	make build-lambda
	aws lambda update-function-code --function-name ${LAMBDA_FUNCTION_NAME} --zip-file fileb://aws_lambda_artifact.zip --region ${AWS_REGION} --profile ${AWS_PROFILE}

# Cluster configurations

create_cluster:
	eksctl create cluster -f deployment/cluster.yaml

delete_cluster:
	eksctl delete cluster -f deployment/cluster.yaml

describe_cluster:
	eksctl utils describe-stacks --region=us-east-2 --cluster=${EKS_CLUSTER_NAME}

aws_identity:
	aws sts get-caller-identity

set_context:
	eksctl utils write-kubeconfig --cluster=${EKS_CLUSTER_NAME} --set-kubeconfig-context=true

enable_iam_sa_provider:
	eksctl utils associate-iam-oidc-provider --cluster=${EKS_CLUSTER_NAME} --approve

create_cluster_role:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/rbac-role.yaml

create_iam_policy:
	curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.0/docs/install/iam_policy.json
	aws iam create-policy \
		--policy-name AWSLoadBalancerControllerIAMPolicy \
		--policy-document file://deployment/iam_policy.json


create_service_account:
	eksctl create iamserviceaccount \
      --cluster=${EKS_CLUSTER_NAME} \
      --namespace=kube-system \
      --name=aws-load-balancer-controller \
      --attach-policy-arn=arn:aws:iam::${AWS_ACCOUNT_ID}:policy/AWSLoadBalancerControllerIAMPolicy \
      --override-existing-serviceaccounts \
      --approve


deploy_cert_manager:
	kubectl apply \
		--validate=false \
		-f https://github.com/jetstack/cert-manager/releases/download/v1.1.1/cert-manager.yaml

install-ingress-nginx-controller:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

k8s-prod-deploy:
	kubectl apply -f deployment/facerek-namespace.yml 
	kubectl apply -f deployment/facerek-secrets.yml 
	kubectl apply -f deployment/facerek-deployment.yml 
	kubectl apply -f deployment/facerek-service.yml

k8s-prod-delete:
	kubectl delete -f deployment/facerek-service.yml
	kubectl delete -f deployment/facerek-deployment.yml 
	kubectl delete -f deployment/facerek-secrets.yml 
	kubectl delete -f deployment/facerek-namespace.yml 

k8s-local-deploy:
	kubectl apply -f deployment/facerek-namespace.yml 
	kubectl apply -f deployment/facerek-namespace.yml 
	kubectl apply -f deployment/facerek-secrets.yml 
	kubectl apply -f deployment/facerek-deployment.yml 
	kubectl apply -f deployment/facerek-service.yml
	kubectl apply -f deployment/facerek-ingress.yml

k8s-update-pods-secrets:
	kubectl apply -f temp/facerek-secrets.yml
	kubectl delete -f deployment/facerek-deployment.yml
	kubectl apply -f deployment/facerek-deployment.yml

facerek-api-pod-bash:
	kubectl exec -it $(kubectl get pod -n facerek -l app=facerek-api -o jsonpath="{.items[0].metadata.name}") -n facerek -- bash

build-frontend:
	(cd frontend; npm ci; npm run build)
	rm -rf ./app/public
	mv ./frontend/build ./app/public