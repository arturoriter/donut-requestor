from donut_requestor.model.donut import Donut, DonutBox


def test_any_donut_of_flavour():
    donut_box = DonutBox(amount=2)
    donut_box.add_donut(Donut(flavour="strawberry"))
    donut_box.add_donut(Donut(flavour="choco"))
    donut_box.add_donut(Donut(flavour="banana"))

    assert donut_box.any_donut_of_flavour(flavour="strawberry")
