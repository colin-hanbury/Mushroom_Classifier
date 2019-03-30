freeze_graph \
 --input_graph=./tf_files/graph.pb \
 --input_checkpoint=./tf_files/model.ckpt-81852 \
 --input_binary=false \
 --output_graph=/tf_files/frozen.pb \
 --output_node_names=input_tensor,output_pred