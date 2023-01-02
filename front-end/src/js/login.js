import axios from "axios";



const login = async(user, password) => {
    const ret = axios.post(`http://localhost/login?user=${user}&password=${password}`).then(r=>r.data).catch(err=>{return err})
    return ret
}

export default login;