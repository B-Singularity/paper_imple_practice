# 1. DAGs 확률적 만들기, DAGS는 만드는 방법 확장 가능성 있음
# 2. 시작점부터 끝점은 고정, 그 사이 경로가 있는지 확인함
# 3. 총 경로수 확인
# 4. b 인수 확인
# 5. 그림으로 확인
# 6. dags를 인코딩 -> 벡터화 -> 벡터값을 이용해 아키텍처 수백만개 생성(병목점)
# 7. 성능 평가후 가장 최적화된 아키텍처의 dags를 출력

# 노드 2개 선택하는 걸 확률로 연결결정

# 명사 클래스, 동사는 매서드,
# DAG 클래스 / 생성자 (입력)
# 인코딩
# 성능평가 -> 일단 집어넣고 나중에 추상화해서 확장 ㄱㄱ
import random

class ProbabilisticDAGGenerator:
    def __init__(self, num_nodes, edge_prob, start_node=1, end_node=None):
        """
        :param num_nodes: Number of nodes in the graph
        :param edge_prob: Edge connection probability between nodes
        :param start_node: Start node (default 1)
        :param end_node: End node (default None)
        """
        self.num_nodes = num_nodes
        self.edge_prob = edge_prob
        self.start_node = start_node
        self.end_node = end_node if end_node is not None else num_nodes
        self.dag = None

    def generate_dags(self, num_edges):
        " 엣지 개수 만큼 확률적으로 연결하기"
        possible_edges = [(i, j) for i in range(1, self.num_nodes + 1) for j in range(i + 1, self.num_nodes + 1)]
        edges = random.sample(possible_edges, num_edges)
        graph = {i: [] for i in range(1, self.num_nodes + 1)}
        for u, v in edges:
            graph[u].append(v)
        return graph





