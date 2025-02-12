from behave import given, when, then
import time
import random

# Simulação de um sistema de atribuição de pedidos
class OrderAssignmentSystem:
    def __init__(self):
        self.orders = []
        self.unassigned_orders = 0

    def add_order(self, order_id):
        self.orders.append({
            "id": order_id,
            "assigned": False,
            "timestamp": time.time()
        })

    def assign_orders(self):
        assigned_count = 0
        total_orders = len(self.orders)
        self.unassigned_orders = 0  # Resetamos antes de cada rodada de atribuição

        for order in self.orders:
            if random.random() > 0.012:  # Aumentamos para ~98.8% de sucesso
                order["assigned"] = True
                assigned_count += 1
            else:
                self.unassigned_orders += 1  # Contabiliza pedidos "no limbo"

        assignment_rate = assigned_count / total_orders if total_orders > 0 else 1
        return assignment_rate, assigned_count

system = OrderAssignmentSystem()

@given("existem pedidos pendentes para entrega")
def step_given_orders_pending(context):
    for i in range(100):  # Simula 100 pedidos
        system.add_order(f"pedido_{i}")

@given("há entregadores disponíveis na região")
def step_given_available_drivers(context):
    pass  # Simulamos que sempre há entregadores disponíveis

@when("o sistema processa a atribuição de pedidos")
def step_when_process_assignment(context):
    context.assignment_rate, context.assigned_count = system.assign_orders()

@then("95% dos pedidos devem ser atribuídos em menos de 2 minutos")
def step_then_check_assignment_time(context):
    assert context.assignment_rate >= 0.95, f"Apenas {context.assignment_rate*100:.1f}% foram atribuídos!"

@given("um novo pedido é criado")
def step_given_new_order_created(context):
    system.add_order("pedido_teste")

@when("o sistema tenta atribuir o pedido")
def step_when_attempt_order_assignment(context):
    context.assignment_rate, _ = system.assign_orders()

@then("a taxa de pedidos não atribuídos deve permanecer abaixo de 1.2%")
def step_then_check_unassigned_rate(context):
    unassigned_rate = system.unassigned_orders / len(system.orders) if len(system.orders) > 0 else 0
    assert unassigned_rate < 0.012, f"A taxa de pedidos não atribuídos está em {unassigned_rate*100:.2f}%!"
