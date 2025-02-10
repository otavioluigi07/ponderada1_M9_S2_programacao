Feature: Distribuição eficiente de pedidos e redução de pedidos "no limbo"

  Como um entregador do Rappi
  Quero que os pedidos sejam atribuídos rapidamente e de forma otimizada
  Para que eu possa maximizar meu tempo e ganhos

  Scenario: Atribuição otimizada de pedidos em menos de 2 minutos
    Given existem pedidos pendentes para entrega
    And há entregadores disponíveis na região
    When o sistema processa a atribuição de pedidos
    Then 95% dos pedidos devem ser atribuídos em menos de 2 minutos

  Scenario: Evitar pedidos "no limbo"
    Given um novo pedido é criado
    When o sistema tenta atribuir o pedido
    Then a taxa de pedidos não atribuídos deve permanecer abaixo de 1.2%
