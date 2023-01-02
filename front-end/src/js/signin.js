import axios from "axios";


const register = async(body) => {
    const requestbody = {
        "database": "admin",
        "collection": "usuarios",
    }
    requestbody['Document'] = body
    console.log(requestbody)
    const ret = axios.post(`http://localhost/signin`, requestbody).then(r=>r.data).catch(err=>{return err})
    return ret
}

export default register;