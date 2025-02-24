import { useForm } from 'react-hook-form';
import { createAtractivo } from '../api/atractivos.api';
import { useState } from 'react';

export function AtractivosFormPage() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [image, setImage] = useState(null);
  const [tipoAtractivo, setTipoAtractivo] = useState(null); // Nuevo estado para el tipo de atractivo


  const onSubmit = async (data) => {
    const formData = new FormData();

    formData.append('place', data.place);
    formData.append('direccion', data.direccion);
    formData.append('artista', data.artista);
    formData.append('lat', data.lat);
    formData.append('lon', data.lon);
    formData.append('referencias', data.referencias);
    formData.append('descripcion', data.descripcion);

    if (image) {
      formData.append('image', image);
    }

    try {
      const res = await createAtractivo(formData);
      console.log(res);
    } catch (error) {
      console.error("Error al crear atractivo:", error);
    }
  };

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleTipoAtractivoChange = (e) => {
    setTipoAtractivo(e.target.value);
  };

  const renderFormulario = () => {
    if (tipoAtractivo) {
      return (
        <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {/* Campos comunes a todos los tipos de atractivos */}
          <div className="mb-4">
            <label htmlFor="place" className="block text-gray-700 text-sm font-bold mb-2">Lugar/Ciudad</label>
            <input type="text" id="place" placeholder="Ingrese el lugar" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("place", { required: true })} />
            {errors.place && <span className="text-red-500 text-xs italic">Este campo es requerido</span>}
          </div>

          <div className="mb-4">
            <label htmlFor="lat" className="block text-gray-700 text-sm font-bold mb-2">Latitud (Opcional)</label>
            <input type="text" id="lat" placeholder="Ingrese la latitud" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("lat")} />
          </div>

          <div className="mb-4">
            <label htmlFor="lon" className="block text-gray-700 text-sm font-bold mb-2">Longitud (Opcional)</label>
            <input type="text" id="lon" placeholder="Ingrese la longitud" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("lon")} />
          </div>


          <div className="mb-4">
            <label htmlFor="direccion" className="block text-gray-700 text-sm font-bold mb-2">Dirección</label>
            <input type="text" id="direccion" placeholder="Ingrese la dirección" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("direccion", { required: true })} />
            {errors.direccion && <span className="text-red-500 text-xs italic">Este campo es requerido</span>}
          </div>

          <div className="mb-4">
            <label htmlFor="referencias" className="block text-gray-700 text-sm font-bold mb-2">Referencias de la Ubicación</label>
            <textarea
              id="referencias"
              placeholder="Ingrese referencias de la ubicación (ej: cerca de la plaza, al lado del supermercado)"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-12"
              {...register("referencias")}
            />
          </div>


          {/* STREET ART */}
          {tipoAtractivo === 'mural' && (
            <>

              <div className="mb-4">
                <label htmlFor="artista" className="block text-gray-700 text-sm font-bold mb-2">Artista (Opcional)</label>
                <input type="text" id="artista" placeholder="Ingrese el artista" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("artista")} /> {/* required quitado */}
              </div>
              <div className="mb-4">
                <label htmlFor="descripcion" className="block text-gray-700 text-sm font-bold mb-2">Descripción del Mural</label>
                <textarea id="descripcion" placeholder="Ingrese una descripción del mural" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-20" {...register("descripcion", { required: true })} />
                {errors.descripcion && <span className="text-red-500 text-xs italic">Este campo es requerido</span>}
              </div>




            </>
          )}

          {/* IGLESIAS */}

          {tipoAtractivo === 'iglesia' && (
            <>
              <div className="mb-4">
                <p className="text-2xl text-red-500">IGLESIAS</p>
                <label htmlFor="nombreParroco" className="block text-gray-700 text-sm font-bold mb-2">Nombre del Párroco</label>
                <input type="text" id="nombreParroco" placeholder="Ingrese el nombre del párroco" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" {...register("nombreParroco", { required: true })} />
                {errors.nombreParroco && <span className="text-red-500 text-xs italic">Este campo es requerido</span>}
              </div>


              {/* ... otros campos específicos para iglesias */}
            </>
          )}

          {/* ... (campos específicos para otros tipos de atractivos) */}

          {/* Campo de imagen (común a todos) */}
          <div className="mb-4 col-span-1 md:col-span-2 lg:col-span-3">
            <label htmlFor="image" className="block text-gray-700 text-sm font-bold mb-2">Imagen</label>
            <input type="file" id="image" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" onChange={handleImageChange} />
            {errors.image && <span className="text-red-500 text-xs italic">Este campo es requerido</span>}
            {image && (
              <div className="mt-2">
                <img src={URL.createObjectURL(image)} alt="Vista previa" className="max-w-full h-auto rounded" />
              </div>
            )}
          </div>

          {/* Botón de guardar (común a todos) */}
          <div className="col-span-1 md:col-span-2 lg:col-span-3 text-center">
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded focus:outline-none focus:shadow-outline">
              Guardar
            </button>
          </div>
        </form>
      );
    }
    return null;
  };


  return (
    <div className="bg-white p-8 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4 text-center">Crear Atractivo Turístico</h2>
      <h2 className="text-lg font-semibold mb-6 text-center text-gray-600">Mural - Iglesia - Naturaleza - Arquitectura - Mirador - Escalera</h2>


      <div className="mb-4">
        <label htmlFor="tipoAtractivo" className="block text-gray-700 text-sm font-bold mb-2">Tipo de Atractivo</label>
        <select
          id="tipoAtractivo"
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          value={tipoAtractivo || ''} // Valor controlado
          onChange={handleTipoAtractivoChange}
        >
          <option value="">Seleccione un tipo de atractivo</option>
          <option value="mural">Mural</option>
          <option value="iglesia">Iglesia</option>
          <option value="naturaleza">Naturaleza</option>
          <option value="arquitectura">Arquitectura</option>
          <option value="mirador">Mirador</option>
          <option value="escalera">Escalera</option>
        </select>
      </div>
      {renderFormulario()} {/* Renderizado condicional del formulario */}


      <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">








      </form>
    </div>
  );
}