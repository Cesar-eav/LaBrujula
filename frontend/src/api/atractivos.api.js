import axios from 'axios'

export const getAllAtractivos = () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/AtractivosTuristicos/')

}

export const getAllAscensores = () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/ascensores/')
}

export const getAllMurales = () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/murales/')

}

export const getAllIglesias = () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/iglesias/')

}

export const getAllEscaleras = () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/escaleras/')
}

export const getAllArquitecturas= () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/arquitectura/')

}

export const getAllMiradores= () => {
    return axios.get('http://127.0.0.1:8000/atractivos/api/v1/miradores/')

}