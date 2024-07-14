### implementacion del servidor
from concurrent import futures
import grpc
import analysis_pb2
import analysis_pb2_grpc
import numpy as np

class DataAnalysisServiceServicer(analysis_pb2_grpc.DataAnalysisServiceServicer):
    def Aggregate(self, request, context):
        data = np.array(request.data)
        response = analysis_pb2.AggregateResponse(
            sum=np.sum(data),
            mean=np.mean(data),
            max=np.max(data),
            min=np.min(data)
        )
        return response
    
    def Filter(self, request, context):
        data = np.array(request.data)
        filtered_data = data[data > request.threshold].tolist()
        response = analysis_pb2.FilterResponse(filtered_data=filtered_data)
        return response

    def Transform(self, request, context):
        data = np.array(request.data)
        transformed_data = (data * 2).tolist()  # Ejemplo simple de transformación
        response = analysis_pb2.TransformResponse(transformed_data=transformed_data)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analysis_pb2_grpc.add_DataAnalysisServiceServicer_to_server(DataAnalysisServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
## -----------------------------------------------------------------------------
# implemetacion del cliente



import grpc
import analysis_pb2
import analysis_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = analysis_pb2_grpc.DataAnalysisServiceStub(channel)
        
        # Prueba del procedimiento Aggregate
        aggregate_request = analysis_pb2.AggregateRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        aggregate_response = stub.Aggregate(aggregate_request)
        print(f"Aggregate result: sum={aggregate_response.sum}, mean={aggregate_response.mean}, "
              f"max={aggregate_response.max}, min={aggregate_response.min}")
        
        # Prueba del procedimiento Filter
        filter_request = analysis_pb2.FilterRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0], threshold=2.5)
        filter_response = stub.Filter(filter_request)
        print(f"Filter result: {filter_response.filtered_data}")
        
        # Prueba del procedimiento Transform
        transform_request = analysis_pb2.TransformRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        transform_response = stub.Transform(transform_request)
        print(f"Transform result: {transform_response.transformed_data}")

if __name__ == '__main__':
    run()
#-----------------------------
## 4. Configuración de seguridad y autenticación

from grpc import UnaryUnaryClientInterceptor

class AuthInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        if 'authorization' not in metadata or metadata['authorization'] != 'valid_token':
            context = grpc.ServicerContext()
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')
        return continuation(handler_call_details)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=(AuthInterceptor(),))
    analysis_pb2_grpc.add_DataAnalysisServiceServicer_to_server(DataAnalysisServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
#-----.------------------------------------------
# Modificación del cliente para incluir el token de autenticación

import grpc
import analysis_pb2
import analysis_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = analysis_pb2_grpc.DataAnalysisServiceStub(channel)
        metadata = (('authorization', 'valid_token'),)
        
        # Prueba del procedimiento Aggregate
        aggregate_request = analysis_pb2.AggregateRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        aggregate_response = stub.Aggregate(aggregate_request, metadata=metadata)
        print(f"Aggregate result: sum={aggregate_response.sum}, mean={aggregate_response.mean}, "
              f"max={aggregate_response.max}, min={aggregate_response.min}")
        
        # Prueba del procedimiento Filter
        filter_request = analysis_pb2.FilterRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0], threshold=2.5)
        filter_response = stub.Filter(filter_request, metadata=metadata)
        print(f"Filter result: {filter_response.filtered_data}")
        
        # Prueba del procedimiento Transform
        transform_request = analysis_pb2.TransformRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        transform_response = stub.Transform(transform_request, metadata=metadata)
        print(f"Transform result: {transform_response.transformed_data}")

if __name__ == '__main__':
    run()
##----------------------------
''' 
5. Optimización de comunicación y pruebas de escalabilidad

    Compresión de datos: gRPC soporta la compresión de mensajes para 
    reducir la latencia de comunicación. Se puede habilitar añadiendo 
    opciones de compresión.'''

## servido 
def serve():
    options = [('grpc.default_compression_algorithm', grpc.CompressionAlgorithm.gzip)]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=options,
                         interceptors=(AuthInterceptor(),))
    analysis_pb2_grpc.add_DataAnalysisServiceServicer_to_server(DataAnalysisServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

##cliente

def run():
    options = [('grpc.default_compression_algorithm', grpc.CompressionAlgorithm.gzip)]
    with grpc.insecure_channel('localhost:50051', options=options) as channel:
        stub = analysis_pb2_grpc.DataAnalysisServiceStub(channel)
        metadata = (('authorization', 'valid_token'),)
        
        # Prueba del procedimiento Aggregate
        aggregate_request = analysis_pb2.AggregateRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        aggregate_response = stub.Aggregate(aggregate_request, metadata=metadata)
        print(f"Aggregate result: sum={aggregate_response.sum}, mean={aggregate_response.mean}, "
              f"max={aggregate_response.max}, min={aggregate_response.min}")
        
        # Prueba del procedimiento Filter
        filter_request = analysis_pb2.FilterRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0], threshold=2.5)
        filter_response = stub.Filter(filter_request, metadata=metadata)
        print(f"Filter result: {filter_response.filtered_data}")
        
        # Prueba del procedimiento Transform
        transform_request = analysis_pb2.TransformRequest(data=[1.0, 2.0, 3.0, 4.0, 5.0])
        transform_response = stub.Transform(transform_request, metadata=metadata)
        print(f"Transform result: {transform_response.transformed_data}")

if __name__ == '__main__':
    run()


