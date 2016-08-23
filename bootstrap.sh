#add_program_name() {
#}


#create the list of installs
declare -a install_list=("emacs")
install_list=("${install_list[@]}" "google-chrome-stable")
install_list=("${install_list[@]}" "google-chrome-stable")
install_list=("${install_list[@]}" "google-chrome-stable")

#perform the actual installations
for pname in "${install_list[@]}"; 
do
	echo "${pname}"
	echo 'sudo apt-get -y install' "${pname}"
done

