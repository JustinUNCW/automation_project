resource "genesyscloud_routing_skill_group" "python_skill_group" {
  name        = "python group"
  description = "Group for agents with a python acd skill > 2"
  skill_conditions = jsonencode([
    {
      "routingSkillConditions" : [
        {
          "routingSkill" : "Python",
          "comparator" : "GreaterThan",
          "proficiency" : 2
          "childConditions" : [
            {
              "routingSkillConditions" : [
                {
                  "routingSkill" : genesyscloud_routing_skill.python_backend_engineer_skill.name
                  "comparator" : "GreaterThan",
                  "proficiency" : 1
                }
              ],
              "operation" : "And",
              "languageSkillConditions" : []
            }
          ]
        }
      ],
      "operation" : "And",
      "languageSkillConditions" : []
    }
  ])
}