import os


class display_mx:
    def save_sa_dot_file(self, path: str, verbose: bool = False) -> None:
        with open(path, "w") as file:
            file.write("digraph G {\n")

            for node_id in self.nodes:
                node = self.get_node_by_id(node_id)
                label = node.get_label

                if node_id in self.inputs:
                    file.write(f"    v{node_id} [color=blue];\n")
                if node_id in self.outputs:
                    file.write(f"    v{node_id} [color=red];\n")

                if verbose:
                    file.write(f'    v{node_id} [label="{label} id={node_id}"];\n')
                else:
                    file.write(f'    v{node_id} [label="{label}"];\n')

                for child_id in node.children:
                    for multiplicity in range(node.children[child_id]):
                        file.write(f"    v{node_id} -> v{child_id};\n")

            file.write("}")

    """
    def from_dot_file
    """

    def display(self, verbose: bool = False) -> None:
        self.save_sa_dot_file("digraph.dot", verbose=verbose)
        os.system("dot -Tpdf digraph.dot -o digraph.pdf")
