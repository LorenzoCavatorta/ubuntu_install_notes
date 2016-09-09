add_program_name() {
    list=$1
    name=$2
    list=("${list[@]}" name)
    return 
}


#create the list of installs
declare -a install_list=("emacs")
install_list=("${install_list[@]}" "google-chrome-stable")
install_list=("${install_list[@]}" "google-chrome-stable")
add_program_name install_list "test"

#perform the actual installations
for pname in "${install_list[@]}"; 
do
	echo "${pname}"
	echo 'sudo apt-get -y install' "${pname}"
done

