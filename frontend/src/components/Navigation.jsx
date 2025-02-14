import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="bg-red-500 flex justify-between items-center p-4">
      <Link to="/">
        <p className="text-2xl w-full">La Brujula</p>
      </Link>
      <div className="flex space-x-4">
        <Link
          to="/atractivos-crear"
          className="text-white hover:text-gray-200 font-bold"
        >
          Crear Atractivo
        </Link>
        <Link to="/ascensores" className="text-white hover:text-gray-200">
          Ascensores
        </Link>
        <Link to="/atractivos" className="text-white hover:text-gray-200">
          Street Art
        </Link>
        <Link to="/arquitectura" className="text-white hover:text-gray-200">
          Arquitectura
        </Link>
        <Link to="/naturalezas" className="text-white hover:text-gray-200">
          Naturaleza
        </Link>
        <Link to="/miradores" className="text-white hover:text-gray-200">
          Miradores
        </Link>
        <Link to="/escaleras" className="text-white hover:text-gray-200">
          Escaleras
        </Link>
        <Link to="/iglesias" className="text-white hover:text-gray-200">
          Iglesias
        </Link>
        {/* <Link
          to="/centros-culturales"
          className="text-white hover:text-gray-200"
        >
          Centros Culturales
        </Link>
        <Link
          to="/centros-culturales"
          className="text-white hover:text-gray-200"
        >
          Plazas
        </Link>
        <Link
          to="/centros-culturales"
          className="text-white hover:text-gray-200"
        >
          Bares
        </Link> */}
      </div>
    </div>
  );
}
