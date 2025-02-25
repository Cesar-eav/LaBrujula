import React, { useState } from "react";
import { Link } from "react-router-dom";

export function AtractivoCard({ atractivo }) {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => {
    console.log("Se hizo clic en la imagen para abrir el modal");
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
  };

  return (
    <div className="flex flex-wrap w-80 p-0 mt-2 bg-gray-800 rounded-lg">
      {/* <h1>{atractivo.title}</h1> */}
      <img src={atractivo.image} onClick={openModal} className="shadow-md"/>


      {modalIsOpen && (
        <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-4 rounded-lg w-1/2 h-5/6 overflow-y-auto">
          <div className="text-black">
          <h1>
          <span className="text-back text-2xl font-bold"> {atractivo.nombre}</span></h1> 
          <h1><span className="text-red-500 font-bold">¿Dónde?</span> {atractivo.place}</h1> 
          <h1><span className="text-red-500 font-bold">Calle:</span> {atractivo.direccion}</h1> 
          <div className="text-justify" dangerouslySetInnerHTML={{ __html: atractivo.content }} />

              </div>
            <img
              src={atractivo.image}
              
            />
            <div className="flex justify-between mx-2 ">
              <button onClick={closeModal} className="bg-red-500 rounded-lg px-2 py-1 mt-1
                ">Cerrar</button>
  
              <Link to={`/mapa/${atractivo.lat}/${atractivo.lon}`} target="_blank">
                <button className="bg-red-800 rounded-lg px-2 py-1 mt-1
                ">Ir al mapa</button>
              </Link>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
