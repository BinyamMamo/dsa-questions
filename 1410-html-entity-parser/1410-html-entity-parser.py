class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        result = []
        i = 0
        n = len(text)

        while i < n:
            if text[i] == "&":
                semicolon = text.find(";", i + 1, i + 10)  # assume 10 max entity length
                if semicolon != -1:
                    candidate = text[i:semicolon + 1]
                    if candidate in entities:
                        result.append(entities[candidate])
                        i = semicolon + 1
                        continue

            result.append(text[i])
            i += 1

        return "".join(result)
