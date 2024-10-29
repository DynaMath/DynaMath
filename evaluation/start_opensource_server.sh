#!/bin/bash
export NCCL_P2P_DISABLE=1 
export NCCL_P2P_DISABLE=1   
export CUDA_VISIBLE_DEVICES=2,3



# Initialize variables with default values (if any)
model_name=""
tp=1
port=23333

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --model_name) 
      if [[ -n $2 && $2 != "--"* ]]; then
        model_name="$2"; 
        shift 
      else
        echo "Error: --model_name requires a non-empty value."
        exit 1
      fi
      ;;
    *)
      echo "Unknown parameter passed: $1"
      exit 1
      ;;
  esac
  shift
done

# Ensure the required argument is provided
if [[ -z $model_name ]]; then
  echo "Error: --model_name is required."
  exit 1
fi


# Check conditions and set tp
if [[ "$model_name" == *"8b"* || "$model_name" == *"8B"* || \
      "$model_name" == *"7b"* || "$model_name" == *"7B"* || \
      "$model_name" == *"9b"* || "$model_name" == *"9B"* || \
      "$model_name" == *"13b"* || "$model_name" == *"13B"* ]]; then
    tp=1
elif [[ "$model_name" == *"26B"* || "$model_name" == *"26b"* || \
        "$model_name" == *"InternVL1.5-Chat"* ]]; then
    tp=2
elif [[ "$model_name" == *"34b"* || "$model_name" == *"34B"* || \
        "$model_name" == *"40B"* || "$model_name" == *"40b"* ]]; then
    tp=4
elif [[ "$model_name" == *"76B"* || "$model_name" == *"76b"* ]]; then
    tp=8
fi

echo $tp
# Start the server
lmdeploy serve api_server "$model_name" --server-port $port --tp $tp