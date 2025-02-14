import { useEffect, useState } from "react";
import { getAllMiradores } from "../api/atractivos.api";
import { AtractivoCard } from "./AtractivoCard";
import Pagination from "react-paginate";



export function MiradoresList() {
  const [atractivos, setAtractivos] = useState([]);
  const [paginaActual, setPaginaActual] = useState(0);
  const atractivosPorPagina = 12;

  useEffect(() => {
    async function loadAtractivos() {
      try {
        const res = await getAllMiradores();
        setAtractivos(res.data);
      } catch (error) {
        console.error(error);
      }
    }
    loadAtractivos();
  }, []);

  const handlePageClick = (event) => {
    setPaginaActual(event.selected);
  };

  const atractivosMostrados = atractivos.slice(
    paginaActual * atractivosPorPagina,
    (paginaActual + 1) * atractivosPorPagina
  );

  return (
    <div>
      <div className="flex flex-wrap gap-4 mx-5 bg-slate-100 justify-center ">
        {atractivosMostrados.map((atractivo) => (
          <AtractivoCard key={atractivo.id} atractivo={atractivo} />
        ))}
      </div>
      <div className="flex text-slate-700 justify-center">
        <Pagination
          pageCount={Math.ceil(atractivos.length / atractivosPorPagina)}
          onPageChange={handlePageClick}
          containerClassName="flex flex-row items-center space-x-2 my-2" // Estilos para el contenedor
          pageClassName="px-3 py-2 rounded-md hover:bg-gray-200" // Estilos para cada página
          pageLinkClassName="text-gray-700" // Estilos para los links de página
          activeClassName="bg-red-500 text-white" // Estilos para la página activa
          previousClassName="px-3 py-2 rounded-md hover:bg-gray-200" // Estilos para "Anterior"
          nextClassName="px-3 py-2 rounded-md hover:bg-gray-200" // Estilos para "Siguiente"
          disabledClassName="text-gray-400 cursor-not-allowed" // Estilos para botones deshabilitados
        />
      </div>
    </div>
  );
}
